from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0


class TestGun(TestCase):

    def setUp(self):
        print(self._testMethodDoc)
   
    def test_lock(self):
        """-- Test Locked Gun"""
        msg = "the gun is unlocked when this is not true"
        self.assertIsNone(Gun.lock(self),msg = msg)
        gun_test = Gun(6)
        self.assertFalse(gun_test.isLock,msg=msg)

    def test_unlock(self):
        """-- Test Unlocked Gun"""
        pass

    def test_isLock(self):
        """-- Test If Gun is Lock"""
        pass

    def test_shoot(self):
        """-- Test Shoot"""
        pass

    def test_reload(self):
        """-- Test Reload """
        pass
