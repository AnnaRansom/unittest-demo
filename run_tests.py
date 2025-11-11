import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    # Find tests starting in the current directory (.)
    tests = loader.discover('.')
    # Verbosity 2 shows each test name and result
    testRunner = unittest.runner.TextTestRunner(verbosity=2)
    testRunner.run(tests)