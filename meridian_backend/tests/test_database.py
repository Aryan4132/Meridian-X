import os
import unittest
import sys
import shutil

# Add meridian_backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Override data dir for testing to prevent polluting production db
        cls.test_dir = os.path.abspath("test_database_dir")
        os.environ["MERIDIAN_DATA_DIR"] = cls.test_dir
        
        # Ensure modules are reimported under the test environment
        for mod in ["src.core.config", "database"]:
            if mod in sys.modules:
                del sys.modules[mod]

    @classmethod
    def tearDownClass(cls):
        # Clean up database dir
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_sqlite_connectivity(self):
        from database import get_sqlite_conn, init_tables
        
        # Init tables
        init_tables()
        
        # Open conn
        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        self.assertIn("user_profile", tables)
        self.assertIn("semantic_cache", tables)
        self.assertIn("conversations", tables)

    def test_user_profile(self):
        from database import save_user_profile, get_user_profile
        
        save_user_profile("test_profile_key", "test_profile_value")
        val = get_user_profile("test_profile_key")
        self.assertEqual(val, "test_profile_value")
        
        # Key that doesn't exist
        self.assertIsNone(get_user_profile("non_existent_key_12345"))

    def test_brain_and_auditor_defaults(self):
        from database import get_brain_model, get_auditor_model
        
        # Unset keys
        brain = get_brain_model()
        auditor = get_auditor_model()
        
        self.assertIsNotNone(brain)
        self.assertIsNotNone(auditor)

if __name__ == "__main__":
    unittest.main()
