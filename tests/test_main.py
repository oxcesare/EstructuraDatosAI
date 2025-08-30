import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # No assertion, just check that main runs without error
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
