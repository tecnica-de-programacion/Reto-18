from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_load_gun(self):
        """-- Test Load Gun"""
        msg = "The ammunition is not being correctly loaded"
        self.assertEqual(Gun(10).reload('hola'), 'hola', msg=msg)
        self.assertEqual(Gun(10).reload(-4), None, msg=msg)
        self.assertEqual(Gun(10).reload(10), 0, msg=msg)
        self.assertEqual(Gun(10).reload(12), 2, msg=msg)

