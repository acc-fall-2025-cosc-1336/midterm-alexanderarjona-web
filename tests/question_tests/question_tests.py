#write function tests here, don't add input('') statements here!
import unittest
import random

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config as test_a_config, use_global, count
from src.question_b.question_b import test_config as test_b_config, get_random_number
from src.question_c.question_c import test_config as test_c_config, use_local_variable
from src.question_d.question_d import test_config as test_d_config, get_day_of_week

class Test_Config(unittest.TestCase):

#A
    def test_question_a_config(self):
        self.assertEqual(True, test_a_config())

    def test_use_global(self):
        global count
        count = 5
        use_global()
        self.assertEqual(count, 6)

#B
    def test_question_b_config(self):
        self.assertEqual(True, test_b_config())

    def test_get_random_number(self):
        for _ in range(10):
            num = get_random_number()
            self.assertTrue(1 <= num <= 5)

#C
    def test_question_c_config(self):
        self.assertEqual(True, test_c_config())

    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        # value should remain unchanged
        self.assertEqual(num, 100)

#D
    def test_question_d_config(self):
        self.assertEqual(True, test_d_config())

    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")

