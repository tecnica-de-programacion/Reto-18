from unittest import TestCase
from mainte import Gun
import sys
sys.tracebacklimit = 0

class Test_Gun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_the_lock_of_gun(self):
        """-- Test the lock of the gun"""
        msg = "The safe of gun is unlock"
        self.assertFalse(Gun.lock(self), msg = msg)

    def test_the_unlock_of_gun(self):
        """-- Test the unlock of the gun"""
        msg= "The safe of gunis lock"
        self.assertFalse(Gun.unlock(self), msg = msg)

    def test_ammount_of_cartridge(self):
        """-- Test ammount of cartridge in the gun"""
        pass

    def test_shoot_gun(self):
        """-- Test shoot gun"""
        pass

    def test_no_cartridge(self):
        """-- Test no cartridge in the gun"""
        pass

    def test_enough_cartridge(self):
        """-- Test enough cartridge"""
        pass

