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

    def test_lock_is_on(self):
        """-- Test Locked Gun"""
        msg = "The gun can't be locked"
        self.gun.lock()
        self.assertEqual(self.gun.isLock, True, msg=msg)

    def test_lock_is_off(self):
        """-- Test Unlocked Gun"""
        msg = "The gun can't be unlocked"
        self.gun.unlock()
        self.assertEqual(self.gun.isLock, False, msg=msg)

    def test_reloading(self):
        """-- Test Correct Reloading Formats"""
        msg = "The gun should only accept integers"
        self.assertEqual(self.gun.reload('hola'), 'hola', msg=msg)
        self.assertEqual(self.gun.reload(-5), None, msg=msg)

    def test_exceding_reloading(self):
        """-- Test Correct Handling Of Number Of Bullets Reloading"""
        msg = "The gun doesn't handle the extra bullets correctly"
        self.assertEqual(self.gun.reload(2), 0, msg=msg)
        self.assertEqual(self.gun.reload(3), 0, msg=msg)
        self.assertEqual(self.gun.reload(2), 2, msg=msg)

    def test_shooting_without_bullets(self):
        """-- Test Shooting Without Bullets"""
        msg = "The gun can shoot without bullets"
        self.gun.unlock()
        self.assertEqual(self.gun.shoot(), None, msg=msg)

    def test_shooting_with_gun_locked(self):
        """-- Test Shooting With Lock On"""
        msg = "The gun can shoot with the safe on"
        self.gun.lock()
        self.gun.reload(1)
        self.assertEqual(self.gun.shoot(), None, msg=msg)

    def test_shooting(self):
        """-- Test Shooting"""
        msg = "The gun can't shoot"
        self.gun.unlock()
        self.gun.reload(5)
        self.gun.shoot()
        self.assertEqual(self.gun._Gun__ammunition, 4, msg=msg)
