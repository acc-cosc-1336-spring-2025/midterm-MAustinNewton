#write function tests here, don't add input('') statements here!
import unittest

# Question 1: Local Variables
from src.question_a.question_a import test_config, use_local_variable

# Question 2: Celsius to Fahrenheit table
from src.question_b.question_b import get_fahrenheit

# Question 3: Sum of Even Numbers
from src.question_c.question_c import get_sum_of_evens

# Question 4: Age Category
from src.question_d.question_d import get_person_category

class Test_Config(unittest.TestCase):

# Question 1: Local Variables
    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)  

# Question 2: Celsius to Fahrenheit table
    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)

# Question 3: Sum of Even Numbers
    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

# Question 4: Age Category
    def test_get_person_category(self):
        self.assertEqual(get_person_category(1), "infant")
        self.assertEqual(get_person_category(2), "child")
        self.assertEqual(get_person_category(14), "teenager")
        self.assertEqual(get_person_category(20), "adult")
        self.assertEqual(get_person_category(-1), "Invalid number")
        self.assertEqual(get_person_category(130), "Invalid number")