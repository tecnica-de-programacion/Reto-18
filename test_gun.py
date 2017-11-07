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