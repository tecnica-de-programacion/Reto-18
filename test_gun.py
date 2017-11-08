from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def shoot(self):
        """test just one bullet for a shoot"""
        self.assertIsInstance(gun(3).shoot(), 2)
        self.assertIsInstance(gun(10).shoot(), 9)

    def charger_empty(self):
        """test can´t shoot if charger is empty"""
        self.assertIsInstance(gun(0).shoot(), None)
        self.assertIsInstance(gun().shoot(), None)

    def charge_bullets(self):
        """ test charging bullets"""
        self.assertIsInstance(gun(12).charger(2), 'cargada')
        self.assertIsInstance(gun(30).charger(28), 'cargada')

    def number_of_bullets(self):
        """ test the bullets that are just posible and bullets wasted"""
        self.assertIsInstance(gun(3).charger(4),1)
        self.assertIsInstance(gun(23).charger(44), 21)

