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
        cls.orig_data_dir = os.environ.get("MERIDIAN_DATA_DIR")
        cls.test_dir = os.path.abspath("test_database_dir")
        os.environ["MERIDIAN_DATA_DIR"] = cls.test_dir

        # Ensure modules are reimported under the test environment
        for mod in list(sys.modules.keys()):
            if mod.startswith("src.db") or mod in ["src.core.config", "database"]:
                del sys.modules[mod]

    @classmethod
    def tearDownClass(cls):
        # Clean up database dir
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
        if cls.orig_data_dir is not None:
            os.environ["MERIDIAN_DATA_DIR"] = cls.orig_data_dir
        elif "MERIDIAN_DATA_DIR" in os.environ:
            del os.environ["MERIDIAN_DATA_DIR"]

    def test_sqlite_connectivity(self):
        from database import get_sqlite_conn, init_tables

        init_tables()

        conn = get_sqlite_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()

        self.assertIn("user_profile", tables)
        self.assertIn("semantic_cache", tables)
        self.assertIn("conversations", tables)
        self.assertIn("thought_logs", tables)
        self.assertIn("knowledge_graph", tables)

    def test_user_profile(self):
        from database import save_user_profile, get_user_profile

        save_user_profile("test_profile_key", "test_profile_value")
        val = get_user_profile("test_profile_key")
        self.assertEqual(val, "test_profile_value")

        self.assertIsNone(get_user_profile("non_existent_key_12345"))

    def test_brain_and_auditor_defaults(self):
        from database import get_brain_model, get_auditor_model

        brain = get_brain_model()
        auditor = get_auditor_model()

        self.assertIsNotNone(brain)
        self.assertIsNotNone(auditor)

    def test_thought_logs_schema_and_operations(self):
        """Verifies thought_logs persists tool_name without schema mismatch crash."""
        from database import add_thought_log, get_thought_logs

        session_id = "test-session-thought-01"
        res = add_thought_log(
            thought_text="Analyzing user query for phishing patterns",
            session_id=session_id,
            step_index=1,
            tool_name="url_detector"
        )
        self.assertTrue(res, "add_thought_log must return True on successful insertion")

        logs = get_thought_logs(session_id=session_id, limit=5)
        self.assertGreaterEqual(len(logs), 1)
        first_log = logs[0]
        self.assertEqual(first_log["session_id"], session_id)
        self.assertEqual(first_log["tool_name"], "url_detector")
        self.assertIn("Analyzing user query", first_log["thought_text"])

    def test_contacts_dual_write(self):
        """Verifies WhatsApp contact is saved to SQLite even when MongoDB is offline."""
        from database import save_whatsapp_contact, get_whatsapp_contacts, resolve_whatsapp_contact

        contact = save_whatsapp_contact(
            name="Alice SecOps",
            phone_number="+1234567890",
            alias="alice",
            notes="Incident commander"
        )
        self.assertEqual(contact["name"], "Alice SecOps")

        contacts = get_whatsapp_contacts()
        names = [c["name"] for c in contacts]
        self.assertIn("Alice SecOps", names)

        resolved = resolve_whatsapp_contact("alice")
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved["phone_number"], "+1234567890")

    def test_knowledge_graph_sqlite_fallback(self):
        """Verifies knowledge facts are persisted and queryable via SQLite fallback."""
        from database import add_knowledge_fact, get_knowledge_facts

        add_knowledge_fact("User", "prefers_theme", "Tokyo Night")
        facts = get_knowledge_facts("User")
        targets = [f["target"] for f in facts]
        self.assertIn("Tokyo Night", targets)

    def test_is_transient_phrase(self):
        """Verifies precompiled transient phrase detection."""
        from database import is_transient_phrase

        self.assertTrue(is_transient_phrase("ok"))
        self.assertTrue(is_transient_phrase("thank you"))
        self.assertTrue(is_transient_phrase("retry."))
        self.assertFalse(is_transient_phrase("Please scan this malicious URL now"))

    def test_semantic_cache_thread_safety(self):
        """Verifies thread-safe caching without concurrent mutation errors."""
        import threading
        from database import add_to_semantic_cache, check_semantic_cache

        errors = []

        def worker(idx):
            try:
                for i in range(10):
                    q = f"test query {idx}_{i}"
                    add_to_semantic_cache(q, f"response {idx}_{i}", ttl_hours=1)
                    res = check_semantic_cache(q)
                    if res != f"response {idx}_{i}":
                        errors.append(f"Cache mismatch for {q}")
            except Exception as e:
                errors.append(str(e))

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(errors), 0, f"Thread safety errors occurred: {errors}")

if __name__ == "__main__":
    unittest.main()
