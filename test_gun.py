from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)



    def test_lock(self):
        """--Test Lock"""
        msg = "It must be true"

        newGun = Gun(10)
        newGun.lock()
        self.assertTrue(newGun.isLock, msg=msg)

    def test_unlock(self):
        """--Test Unlock"""
        msg = "It must be false"
        newGun = Gun(10)
        newGun.unlock()
        self.assertFalse(newGun.isLock, msg=msg)

    def test_isLock(self):
        """-- Test isLock"""
        msg = 'To be able to shoot it is necessary that isLock == False'

        newGun = Gun(10)
        newGun.isLock()
        self.assertFalse(newGun.isLock, msg=msg)


    def test_shoot(self):
        """--Test shoot"""
        msg = "The weapon does not work"

        newGun = Gun(10)
        self.assertEqual(newGun.shoot(), "Gun is empty", msg=msg)
        newGun.reload(7)
        self.assertEqual(newGun.shoot(), 6, msg=msg)
        newGun.lock()
        self.assertEqual(newGun.shoot(), "Gun is lock", msg=msg)

    def test_reload(self):
        """--Test reload"""
        msg = "It is not possible to reload ammunition"

        newGun = Gun(10)
        self.assertEqual(newGun.reload(-10), None, msg=msg)
        self.assertEqual(newGun.reload(10.56), 10.56, msg=msg)
        self.assertEqual(newGun.reload(15), 5, msg=msg)