import os
import unittest
import sys
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestLLMProvider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Prevent test db pollution
        os.environ["MERIDIAN_DATA_DIR"] = os.path.abspath("test_llm_provider_dir")

    @classmethod
    def tearDownClass(cls):
        import shutil
        test_dir = os.path.abspath("test_llm_provider_dir")
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

    def run_async(self, coro):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coro)
        finally:
            loop.close()

    @patch("src.core.llm_provider.httpx.AsyncClient")
    def test_ollama_stream_success(self, mock_client_class):
        from src.core.llm_provider import generate_completion_stream
        
        # Mock Response and iter_lines
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # Async stream lines mock
        async def mock_iter_lines():
            yield b'{"message": {"content": "Hello"}}'
            yield b'{"message": {"content": " world!"}}'
            
        mock_response.iter_lines = mock_iter_lines
        
        # Mock Client
        mock_client = MagicMock()
        
        # Async context manager stream mock
        class MockStreamContext:
            async def __aenter__(self):
                return mock_response
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass
                
        mock_client.stream.return_value = MockStreamContext()
        
        # Async context manager client mock
        class MockClientContext:
            async def __aenter__(self):
                return mock_client
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass
                
        mock_client_class.return_value = MockClientContext()

        # Run stream and collect outputs
        async def run_stream():
            chunks = []
            async for chunk in generate_completion_stream(
                messages=[{"role": "user", "content": "Hi"}],
                provider="ollama",
                model="qwen"
            ):
                chunks.append(chunk)
            return chunks

        results = self.run_async(run_stream())
        self.assertEqual("".join(results), "Hello world!")

    @patch("src.core.llm_provider.get_api_key")
    @patch("src.core.llm_provider.httpx.AsyncClient")
    def test_remote_failure_raises_error(self, mock_client_class, mock_get_api_key):
        from src.core.llm_provider import generate_completion_stream
        
        # Set api keys so it doesn't fail onboarding checks
        mock_get_api_key.return_value = "dummy_key"
        
        # Setup Client to fail with connection error for openai url
        mock_openai_response = MagicMock()
        mock_openai_response.status_code = 500
        mock_openai_response.aread = AsyncMock(return_value=b"Internal Server Error")
        
        class DynamicStreamContext:
            def __init__(self, method, url, **kwargs):
                self.url = url
            async def __aenter__(self):
                return mock_openai_response
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass

        mock_client = MagicMock()
        mock_client.stream.side_effect = DynamicStreamContext
        
        class MockClientContext:
            async def __aenter__(self):
                return mock_client
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass
        
        mock_client_class.return_value = MockClientContext()

        # Run stream and collect
        async def run_stream():
            chunks = []
            async for chunk in generate_completion_stream(
                messages=[{"role": "user", "content": "Hi"}],
                provider="openai",
                model="gpt-4"
            ):
                chunks.append(chunk)
            return chunks

        results = self.run_async(run_stream())
        combined = "".join(results)
        
        self.assertIn("Remote provider openai call failed", combined)

if __name__ == "__main__":
    unittest.main()
