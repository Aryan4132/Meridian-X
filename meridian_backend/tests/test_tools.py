import os
import unittest
import sys
import json
import shutil

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = os.path.abspath("test_tools_dir")
        os.environ["MERIDIAN_DATA_DIR"] = cls.test_dir
        
        # Override workspace CWD for test environment
        if "src.core.config" in sys.modules:
            del sys.modules["src.core.config"]

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_tool_registry(self):
        from src.tools.registry import TOOL_REGISTRY
        
        # Ensure standard tools are loaded
        self.assertIn("read_file", TOOL_REGISTRY)
        self.assertIn("write_file", TOOL_REGISTRY)
        self.assertIn("nl_run", TOOL_REGISTRY)

    def test_audit_logging_file_write(self):
        from src.tools.filesystem import write_file
        from src.core.audit_logger import get_audit_log_path
        
        target_path = os.path.join(self.test_dir, "test_audit.txt")
        write_file(target_path, "Audit test data")
        
        audit_path = get_audit_log_path()
        self.assertTrue(os.path.exists(audit_path))
        
        # Verify log entry structure
        with open(audit_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        last_line = json.loads(lines[-1])
        self.assertEqual(last_line["category"], "FILE_WRITE")
        self.assertEqual(last_line["action"], "write_file")
        self.assertEqual(last_line["details"]["path"], target_path)
        self.assertEqual(last_line["status"], "SUCCESS")

    def test_audit_logging_shell_blocked(self):
        from src.tools.shell import nl_run
        from src.core.audit_logger import get_audit_log_path
        
        # Trigger blocked command pattern
        res = nl_run("format C:")
        self.assertIn("Blocked execution", res)
        
        audit_path = get_audit_log_path()
        with open(audit_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # Parse last audit log line
        last_line = json.loads(lines[-1])
        self.assertEqual(last_line["category"], "SHELL_EXECUTION")
        self.assertEqual(last_line["status"], "BLOCKED")
        self.assertIn("Safety Gate", last_line["details"]["reason"])

if __name__ == "__main__":
    unittest.main()
