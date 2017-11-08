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
        msg = "attribute isLock expect 'False'"
        self.assertIsNone(Gun.unlock(self), msg=msg)
        gun_test = Gun(6)
        gun_test.unlock()
        self.assertFalse(gun_test.isLock,msg=msg)

    def test_isLock(self):
        """-- Test If Gun is Lock"""
        msg = "isLock is not return the value expect"
        gun_test = Gun(6)
        self.assertFalse(gun_test.isLock,msg = msg)

    def test_shoot(self):
        """-- Test Shoot"""
        msg = "the correct value is not the expect"
        gun_test = Gun(6)
        self.assertEqual(gun_test.shoot(),None, msg=msg)
        gun_test.reload(2)
        self.assertEqual(gun_test.shoot(),None, msg=msg)
        gun_test.lock()
        self.assertEqual(gun_test.shoot(), None, msg=msg)

    def test_reload(self):
        """-- Test Reload """
        msg = "ERROR, value entry is not valid"
        self.assertEqual(Gun.reload(self, int), int, msg=msg)
        gun_test = Gun(6)
        self.assertEqual(gun_test.reload(6),0, msg=msg)
        self.assertEqual(gun_test.reload(10),10,msg=msg)
        self.assertEqual(gun_test.reload(-1),None,msg=msg)
