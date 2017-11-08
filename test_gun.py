from unittest import TestCase
from mainte import Gun
import sys
sys.tracebacklimit = 0
one_gun = Gun(10)

class Test_Gun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_lock_gun(self):
        """-- Test lokc gun"""
        msg = "The gun is unlock"
        one_gun.lock()
        self.assertTrue(one_gun.isLock, msg = msg)

    def test_the_lock_of_gun(self):
        """-- Test the lock of the gun"""
        msg = "The safe of gun is unlock"
        one_gun.unlock()
        self.assertFalse(one_gun.isLock, msg = msg)

    def test_correct_type_safe(self):
        """-- Test correct type of safe"""
        msg = "The correct value for bool is not returned"
        self.assertIsInstance(one_gun.isLock, bool, msg = msg)

    def test_gun_shoot(self):
        """-- Test gun shoot"""
        msg = "The gun can shoot because the safe is open"
        one_gun.shoot()
        self.assertFalse(one_gun.isLock, msg = msg)


    def test_reload_gun(self):
        """-- Test reload gun"""
        msg = "The gun can not reload"
        self.assertEquals(one_gun.reload(9),0,msg= msg)


