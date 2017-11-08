from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_load_gun(self):
        """-- Test the gun reoading"""
        msg = "The amunation reloading doesnt work correctly"
        self.assertEqual(Gun(30).reload('zorro'), 'zorro', msg=msg)
        self.assertEqual(Gun(30).reload('@35'), '@35', msg=msg)
        self.assertEqual(Gun(30).reload(-4), None, msg=msg)
        self.assertEqual(Gun(30).reload(3.1416), None, msg=msg)
        self.assertEqual(Gun(30).reload(40), 10, msg=msg)
        self.assertEqual(Gun(30).reload(15), 0, msg=msg)


    def test_locking(self):
        """-- Test gun locking"""
        msg = "The locking/unlocking system doesnt work correctly"
        desert_eagle = Gun(12)
        self.assertEqual(desert_eagle.isLock, False, msg=msg)
        desert_eagle.lock()
        self.assertEqual(desert_eagle.isLock, True, msg=msg)
        desert_eagle.unlock()
        self.assertEqual(desert_eagle.isLock, False, msg=msg)


    def test_gun_shooting(self):
        """-- Test gun shooting"""
        msg = "The gun doesnt shoot correctly"
        desert_eagle = Gun(12)
        self.assertEqual(desert_eagle.shoot(), None, msg=msg)
        desert_eagle.reload(3)
        desert_eagle.lock()
        self.assertEqual(desert_eagle.shoot(), None, msg=msg)
        desert_eagle.unlock()
        self.assertEqual(desert_eagle.shoot(), 2, msg=msg)
