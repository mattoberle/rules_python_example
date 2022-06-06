import unittest


class ExampleTest(unittest.TestCase):
    def test_import_sqlalchemy(self):
        try:
            import sqlalchemy
        except ImportError:
            self.fail("Package 'sqlalchemy' not found.")

    def test_import_psycopg2(self):
        try:
            import psycopg2
        except ImportError:
            self.fail("Package 'psycopg2' not found.")


if __name__ == "__main__":
    unittest.main()
