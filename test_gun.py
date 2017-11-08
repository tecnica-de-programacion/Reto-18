from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_object_creation(self):
        """--- Test Object Creation ---"""
        msg = "The object creation is not working well."
        gun = Gun(5)
        self.assertEqual(gun._Gun__isLock, False, msg = msg)
        self.assertEqual(gun._Gun__cartridge_size, 5, msg = msg)
        self.assertEqual(gun._Gun__ammunition, 0, msg = msg)

    def test_lock_unlock(self):
        """--- Test Lock and Unlock ---"""
        msg = "The Lock or Unlock function is not working well."
        gun = Gun(5)
        self.assertEqual(gun.isLock, False, msg = msg)
        gun.lock()
        self.assertEqual(gun.isLock, True, msg = msg)
        gun.unlock()
        self.assertEqual(gun.isLock, False, msg = msg)

    def test_reload(self):
        """--- Test Reload ---"""
        msg = "The Reload function is not working well."
        gun = Gun(5)
        self.assertEqual(gun.reload(4.3), 4.3, msg = msg)
        self.assertEqual(gun.reload(-4), None, msg = msg)
        self.assertEqual(gun.reload(6), 1, msg = msg)
        self.assertEqual(gun._Gun__ammunition, 5, msg = msg)

    def test_shoot(self):
        """--- Test Shoot ---"""
        msg = "The Shoot function is not working well"
        gun = Gun(5)
        gun.lock()
        self.assertEqual(gun.shoot(), None, msg = msg)
        gun.unlock()
        self.assertEqual(gun.shoot(), None, msg = msg)
        gun.reload(5)
        self.assertEqual(gun.shoot(), None, msg = msg)
        self.assertEqual(gun._Gun__ammunition, 4, msg=msg)
