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

    def test_gun_locked(self):
        """-- Test if the gun is locked"""
        msg = "The gun is not being correctly locked"
        magnum = Gun(1)
        self.assertEqual(magnum.isLock, False, msg=msg)
        magnum.lock()
        self.assertEqual(magnum.isLock, True, msg=msg)
        magnum.unlock()
        self.assertEqual(magnum.isLock, False, msg=msg)

    def test_gun_shoot(self):
        """-- Test if the gun shoots correctly"""
        msg = "The gun is not shooting correctly"
        magnum = Gun(1)
        self.assertEqual(magnum.shoot(), None, msg=msg)
        magnum.reload(1)
        magnum.lock()
        self.assertEqual(magnum.shoot(), None, msg=msg)
        magnum.unlock()
        self.assertEqual(magnum.shoot(), 0, msg=msg)