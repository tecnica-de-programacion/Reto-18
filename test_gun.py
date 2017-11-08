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


    def test_the_unlock_of_gun(self):
        """-- Test the unlock of the gun"""
        msg= "The safe of gun is lock"

    def test_shoot_gun(self):
        """-- Test shoot gun"""
        msg = "When the gun shoot the safe must lock"


    def test_no_cartridge(self):
        """-- Test no cartridge in the gun"""
        pass

    def test_enough_cartridge(self):
        """-- Test enough cartridge"""
        pass

