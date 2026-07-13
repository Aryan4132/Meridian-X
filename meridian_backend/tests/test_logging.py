import os
import unittest
import sys
import logging
import shutil

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestLogging(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.abspath("test_logging_dir")
        os.environ["MERIDIAN_DATA_DIR"] = self.test_dir
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Override workspace CWD for test environment pathing
        if "src.core.config" in sys.modules:
            del sys.modules["src.core.config"]
        if "src.core.logging_config" in sys.modules:
            del sys.modules["src.core.logging_config"]
        if "src.core.audit_logger" in sys.modules:
            del sys.modules["src.core.audit_logger"]

    def tearDown(self):
        # Shutdown logging to release handles first
        try:
            from src.core.logging_config import shutdown_logger
            shutdown_logger()
        except Exception:
            pass
            
        # Clean up directory
        if os.path.exists(self.test_dir):
            try:
                shutil.rmtree(self.test_dir)
            except Exception as e:
                print(f"Failed to clean up test directory: {e}")
                
        # Clean up environment variables
        if "MERIDIAN_DATA_DIR" in os.environ:
            del os.environ["MERIDIAN_DATA_DIR"]
            
        # Reset logging system to default state
        root_logger = logging.getLogger()
        for handler in list(root_logger.handlers):
            root_logger.removeHandler(handler)

    def test_setup_logger_creates_file(self):
        from src.core.logging_config import setup_logger, shutdown_logger
        
        # Setup logging
        log_file = setup_logger()
        self.assertTrue(os.path.exists(log_file))
        self.assertIn("test_logging_dir", log_file)
        
        # Write log
        logging.info("Meridian-X logging test success message")
        
        # Check that file has content
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Meridian-X logging test success message", content)
        
        # Shutdown logger and delete file
        shutdown_logger()
        
        try:
            os.remove(log_file)
            deleted = True
        except PermissionError:
            deleted = False
            
        self.assertTrue(deleted, "Expected to be able to delete the log file after shutdown_logger")

    def test_audit_logger_uses_data_dir(self):
        from src.core.audit_logger import get_audit_log_path, log_sensitive_action
        
        audit_path = get_audit_log_path()
        self.assertIn("test_logging_dir", audit_path)
        
        # Log action
        log_sensitive_action(
            category="TEST_CATEGORY",
            action="test_action",
            details={"test_key": "test_value"},
            status="SUCCESS"
        )
        
        self.assertTrue(os.path.exists(audit_path))
        with open(audit_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        import json
        last_line = json.loads(lines[-1])
        self.assertEqual(last_line["category"], "TEST_CATEGORY")
        self.assertEqual(last_line["action"], "test_action")
        self.assertEqual(last_line["details"]["test_key"], "test_value")

if __name__ == "__main__":
    unittest.main()
