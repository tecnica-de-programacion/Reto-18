from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)
        self.gun = Gun(5)

    def tearDown(self):
        pass

    def test_lock(self):
        """-- Test Gun Lock"""
        msg = "The gun is not lock"
        self.gun.lock()
        self.assertTrue(self.gun.isLock, msg = msg)

    def test_unlock(self):
        """-- Test Gun is Unlock"""
        msg ="The gun is lock"
        self.gun.unlock()
        self.assertFalse(self.gun.isLock, msg = msg)

    def test_isLock(self):
        pass

    def test_shoot(self):
        pass

    def test_reload(self):
        """-- Test Reloading """
        msg = "Failed reloading"
        self.assertIsNone(self.gun.reload(-5), msg = msg)
        self.assertIsInstance(self.gun.reload(5.5), float, msg = msg)
        self.assertIsInstance(self.gun.reload(5), int, msg = msg)
