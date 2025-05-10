import unittest 

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):
    def test_get_rolled_value(self):
        die = Die()

        for i in range(0,3):
                die.roll()
                rolled_value = die.get_rolled_value()
                self.assertEqual(rolled_value >= 1 , True)
                self.assertEqual(rolled_value <= 6 , True)