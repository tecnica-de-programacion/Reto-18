from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)
        self.gun = Gun(7)

    def test_lock(self):
        """-- Gun Lock Test """
        msg = "The lock works"
        self.gun.lock()
        self.assertIs(self.gun.isLock, True, msg = msg)

    def test_unlock(self):
        """-- Gun is Unlock Test """
        msg = "The unlock works"
        self.gun.unlock()
        self.assertIs(self.gun.isLock, False, msg = msg)

    def test_isLock(self):
        """-- Calling is Lock Test"""
        msg = "Problem with isLock"
        self.assertIsNotNone(self.gun.isLock, msg = msg)

    def test_shoot(self):
        """-- Shooting Test"""
        msg = "The shooting has an error"
        self.gun.lock()
        self.assertIsNone(self.gun.shoot(), msg = msg)
       
        self.gun.reload(2)
        self.gun.shoot()
        self.assertEqual(self.gun.reload(8), 2, msg=msg)


    def test_reload(self):
        """-- Reloading Test """
        msg = "Reloading Error"
        self.assertIsNone(self.gun.reload(-5), msg = msg)
        self.assertNotIsInstance(self.gun.reload(7.8), int, msg=msg)
        self.assertNotIsInstance(self.gun.reload("five"), int, msg=msg)
        self.assertIsInstance(self.gun.reload(7), int, msg=msg)
        self.assertEqual(self.gun.reload(3), 3, msg=msg)


