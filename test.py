def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    test()
