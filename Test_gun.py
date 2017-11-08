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
        msg = "Error with function isLock"
        self.assertIsNotNone(self.my_gun.isLock, msg=msg)



    def test_lock_gun(self):
        """Test, lock my gun"""
        msg = "My gun has not locked"
        self.my_gun.lock()
        self.assertIs(self.my_gun.isLock, True, msg=msg)

    def test_unLock_gun(self):
        """Test, unlock my gun"""
        msg = "My gun is lock yet"
        self.my_gun.unlock()
        self.assertIs(self.my_gun.isLock, False, msg=msg)


    def test_shooting_gun(self):
        """Test, shooting my gun"""
        msg = "Fail shoot"
        self.my_gun.lock()
        self.assertIsNone(self.my_gun.shoot(), msg=msg)




    def test_reload_gun(self):
        """Test, reload my gun"""
        msg = "Fail reload"
        self.assertNotIsInstance(self.my_gun.reload(23.09), int, msg=msg)
        self.assertIsNone(self.my_gun.reload(-99), msg=msg)
        self.assertIsInstance(self.my_gun.reload(10), int, msg=msg)



