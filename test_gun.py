from unittest import TestCase
from main import Gun
import sys

sys.tracebacklimit = 0


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_lock(self):
        """--Test Lock"""
        msg = "The lock is wrong"
        demo_gun = Gun(6)
        demo_gun.lock()
        self.assertEqual(demo_gun.isLock, True, msg=msg)

    def test_unlock(self):
        """--Test Unlock"""
        msg = "The lock is wrong"
        demo_gun = Gun(6)
        demo_gun.unlock()
        self.assertEqual(demo_gun.isLock, False, msg=msg)

    def test_shoot(self):
        """--Test shoot"""
        msg = "Your gun isnt shooting, smthg wrong tho :("
        demo_gun = Gun(6)
        self.assertEqual(demo_gun.shoot(), "Gun is empty", msg=msg)
        demo_gun.reload(4)
        self.assertEqual(demo_gun.shoot(), 3, msg=msg)
        demo_gun.lock()
        self.assertEqual(demo_gun.shoot(), "Gun is lock", msg=msg)

    def test_reload(self):
        """--Test reload"""
        msg = "You cant even reload your gun :("
        gun = Gun(6)
        self.assertEqual(gun.reload(-1), None, msg=msg)
        self.assertEqual(gun.reload(20.2), 20.2, msg=msg)
        self.assertEqual(gun.reload(7), 1, msg=msg)

