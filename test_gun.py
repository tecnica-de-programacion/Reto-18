from unittest import TestCase
from mainte import Gun
import sys
sys.tracebacklimit = 0

class TestFormater(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_the_safe_is_unlock(self):
        """-- Test is unlock the gun"""
        pass

    def test_empty_gun(self):
        """-- Test empty gun"""
        pass

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

