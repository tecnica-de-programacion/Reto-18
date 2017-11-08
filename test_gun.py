from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def test_lock(self):
        """--Test Lock"""
        msg = "The posicion of the lock is wrong"
        gun =Gun(5)
        gun.lock()
        self.assertTrue(gun.isLock, msg =msg)

    def test_unlock(self):
        """--Test Unlock"""
        msg = "The posicion of the lock is wrong"
        gun = Gun(5)
        gun.unlock()
        self.assertFalse(gun.isLock, msg =msg)

    def test_shoot(self):
        """--Test shoot"""
        msg = "The shoot is not done correctly. The correct value is not being returned"
        gun = Gun(10)
        self.assertEqual(gun.shoot(), "Gun is empty", msg=msg)
        gun.reload(5)
        self.assertEqual(gun.shoot(), 4, msg=msg)
        gun.lock()
        self.assertEqual(gun.shoot(), "Gun is lock", msg=msg)

    def test_reload(self):
        """--Test reload"""
        msg = "The reload is not done correctly. The correct value is not being returned"
        gun = Gun(10)
        self.assertEqual(gun.reload(10.5), 10.5, msg=msg)
        self.assertEqual(gun.reload(-10), None, msg=msg)
        self.assertEqual(gun.reload(20), 10, msg=msg)
