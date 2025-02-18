
import unittest
from src.homework.c_decisions.decisions import get_options_ratio

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(get_options_ratio(5,2,2.5), True)

