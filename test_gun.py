from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)
        self.gun = Gun(5)

    def test_lock(self):
        """-- Test Gun Lock"""
        msg = "The gun is not lock"
        self.gun.lock()
        self.assertIs(self.gun.isLock, True, msg = msg)

    def test_unlock(self):
        """-- Test Gun is Unlock"""
        msg = "The gun is lock"
        self.gun.unlock()
        self.assertIs(self.gun.isLock, False, msg = msg)

    def test_isLock(self):
        """-- Test Calling is Lock"""
        msg = "Problem calling isLock"
        self.assertIsNotNone(self.gun.isLock, msg = msg)

    def test_shoot(self):
        """-- Test Shooting"""
        msg = "The shooting is failing"
        self.gun.lock()
        self.assertIsNone(self.gun.shoot(), msg = msg)

    def test_reload(self):
        """-- Test Reloading """
        msg = "Failed reloading"
        self.assertIsNone(self.gun.reload(-5), msg = msg)
        self.assertNotIsInstance(self.gun.reload(5.5), int, msg = msg)
        self.assertNotIsInstance(self.gun.reload("five"), int, msg = msg)
        self.assertIsInstance(self.gun.reload(5), int, msg = msg)
