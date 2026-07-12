import os
import unittest
import sys

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.original_data_dir = os.environ.get("MERIDIAN_DATA_DIR")
        
    def tearDown(self):
        if self.original_data_dir is not None:
            os.environ["MERIDIAN_DATA_DIR"] = self.original_data_dir
        elif "MERIDIAN_DATA_DIR" in os.environ:
            del os.environ["MERIDIAN_DATA_DIR"]

    def test_data_dir_resolution(self):
        # Set a dummy data dir
        test_dir = os.path.abspath("dummy_test_data_dir")
        os.environ["MERIDIAN_DATA_DIR"] = test_dir
        
        # Reload/reimport config module to verify it picks it up
        if "src.core.config" in sys.modules:
            del sys.modules["src.core.config"]
            
        from src.core.config import DB_DIR, MERIDIAN_DATA_DIR
        
        self.assertEqual(MERIDIAN_DATA_DIR, test_dir)
        self.assertTrue(os.path.exists(test_dir))
        self.assertTrue(os.path.exists(DB_DIR))
        
        # Clean up created directories
        try:
            os.rmdir(DB_DIR)
            os.rmdir(test_dir)
        except Exception:
            pass

if __name__ == "__main__":
    unittest.main()
