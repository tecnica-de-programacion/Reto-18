from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0
magnum = Gun(10)

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_lock(self):
        """-- Test Lock Gun"""
        msg = "The Gun is not being locked"
        magnum.lock()
        self.assertTrue(magnum.isLock, msg=msg)

    def test_unlock(self):
        """-- Test unlock Gun"""
        msg = "The Gun is not being unlocked"
        magnum.unlock()
        self.assertFalse(magnum.isLock, msg=msg)

    def test_isLock(self):
        """-- Test Int isLock"""
        msg = "The correct type is not being returned for isLock"
        self.assertIsInstance(magnum.isLock, bool, msg=msg)

    def test_shoot(self):
        """-- Test shoot gun"""
        msg = "The gun is not shooting"
        msg_2 = "The gun is shooting locked"
        self.assertTrue(magnum.shoot, msg=msg)
        magnum.lock()
        self.assertTrue(magnum.shoot, msg = msg_2)