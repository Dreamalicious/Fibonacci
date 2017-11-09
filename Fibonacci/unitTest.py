import unittest
import fibonacci

class UnitTests(unittest.TestCase):
    '''
        Unit tests for Fibonacci Number Calculator:

            Fib(20) = 6765
            Fib(10) = 55

        Results verified by Wolfram Alpha: https://www.wolframalpha.com
    '''

    def testFib(self):
        self.assertEqual(fibonacci.fib(20), 6765)
        self.assertEqual(fibonacci.fib(10) , 55)
        self.assertEqual(fibonacci.fib(0), 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
