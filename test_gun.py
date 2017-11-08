from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        self.gun = Gun(7)
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_lock(self):
        """-- Test Lock"""
        msg = "The lock posicion is wrong"
        gun = Gun(7)
        self.gun.lock()
        self.assertTrue(self.gun.isLock, msg=msg)

    def test_unlock(self):
        """-- Test Unlock"""
        msg = "The lock posicion is wrong"
        gun = Gun(7)
        self.gun.unlock()
        self.assertFalse(self.gun.isLock, msg=msg)

    def test_shoot(self):
        """-- Test Shoot"""
        msg = "The gun can not shoot"
        gun = Gun(7)
        self.gun.reload(4)
        self.assertEqual(self.gun.shoot(), None, msg=msg)
        self.gun.lock()
        self.assertEqual(self.gun.shoot(), None, msg=msg)
        self.gun.unlock()
        self.assertEqual(self.gun.shoot(), None, msg=msg)


    def test_reload(self):
        """-- Test Reload"""
        msg = "The gun can not shoot"
        gun = Gun(7)
        self.assertEqual(self.gun.reload(12), 5, msg=msg)
        self.assertEqual(self.gun.reload(4.8), 4.8, msg=msg)
        self.assertEqual(self.gun.reload(-15), None, msg=msg)

