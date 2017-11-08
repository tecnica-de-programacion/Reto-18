from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class Test_my_Gun(TestCase):

    def setUp(self):
        print(self._testMethodDoc)
        self.my_gun = Gun(100)

    def test_is_Lock_gun(self):
        """Test, is lock my gun?"""
        pass

    def test_unLock_gun(self):
        """Test, unlock my gun"""
        pass

    def test_lock_gun(self):
        """Test, lock my gun"""
        pass


    def test_shooting_gun(self):
        """Test, shooting my gun"""
        pass



    def test_reload_gun(self):
        pass



