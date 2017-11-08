from unittest import TestCase
from main import Gun
import sys

sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        self.gun = Gun(5)

    def test_lock(self):
        """-- Test Gun Lock"""
        msg = "The lock position in the gun is incorrect"
        self.gun.lock()
        self.assertTrue(self.gun.isLock, msg = msg)

    def test_unlock(self):
        """-- Test Gun Unlock"""
        msg = "The lock position in the gun is incorrect"
        self.gun.unlock()
        self.assertFalse(self.gun.isLock, msg = msg)

    def test_shoot(self):
        """-- Test Gun Shoot"""
        msg = "The gun can't shoot correctly"
        self.gun.reload(1)
        self.gun.lock()
        self.assertEqual(self.gun.shoot(), None, msg = msg)
        self.gun.unlock()
        self.assertEqual(self.gun.shoot(), None, msg = msg)
        self.assertEqual(self.gun.shoot(), None, msg = msg)

    def test_reload(self):
        """-- Test Gun Reload"""
        msg = "The gun can't reload correctly"
        self.assertEqual(self.gun.reload(5), 0, msg = msg)
        self.assertEqual(self.gun.reload(-2), None, msg = msg)
        self.assertEqual(self.gun.reload(6.2), 6.2, msg = msg)