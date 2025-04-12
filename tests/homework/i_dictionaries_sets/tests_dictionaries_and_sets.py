import unittest 

from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        inventory = dict()
        widget = 'Widget1'
        quantity = 10

        self.assertEqual(add_inventory(inventory, widget, quantity), {'Widget1' : 10})
        self.assertEqual(add_inventory(inventory, 'Widget1', 25), {'Widget1' : 35})
        self.assertEqual(add_inventory(inventory, 'Widget1', -10), {'Widget1': 25})

    def test_remove_inventory(self):
        inventory = {'Widget1' : 10, 'Widget2' : 20}

        self.assertEqual(remove_inventory(inventory, 'Widget1'), {'Widget2' : 20})

        numinventory = len(inventory)
        self.assertEqual(numinventory, 1)