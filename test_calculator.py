#https://github.com/wille1773-hash/lab11-WE-MN.git
#Partner1: William Evans
#Partner2: Matthew Nunes
import sys, os
sys.path.append(os.path.dirname(__file__))
import unittest
from calculator import *
import calculator
import math

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2,2),4)
        self.assertEqual(calculator.add(12,73),85)
        self.assertEqual(calculator.add(1,9),10)


    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.sub(10,5),5)
        self.assertEqual(calculator.sub(100,5),95)
        self.assertEqual(calculator.sub(2,1),1)


    ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10,0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.log(2,4), math.log(4,2))
        self.assertEqual(calculator.log(10,100), math.log(100,10))
        self.assertEqual(calculator.log(2,16), math.log(16,2))


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            calculator.log(1,17)
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()