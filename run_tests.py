import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.j_classes.tests_classes import Test_Config

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Config)

unittest.TextTestRunner().run(suite)