from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0
Gun_test = Gun(5)


class TestGun(TestCase):

    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_islock(self):
        """--Test is lock"""
        message = " The value is not a bool"
        self.assertIsInstance(Gun_test.isLock, bool, msg = message)


    def test_lock(self):
        """--Test lock"""
        message = "The gun is not locked"
        Gun_test.lock()
        self.assertEqual(Gun_test.isLock, True, msg = message)


    def test_unlock(self):
        """--Test unlock"""
        message = "The gun is locked"
        Gun_test.unlock()
        self.assertEqual(Gun_test.isLock, False, msg = message)


    def test_correct_reload(self):
        """--Test reload """
        message = "Incorrect value of ammunition"
        Gun_test.reload(5)
        self.assertEqual(Gun_test.get_ammunition, 5, msg = message)


    def test_invalid_reload(self):
        """"--Test bullets exceed cartridge size"""
        message = "Incorrect value "
        self.assertEqual(Gun_test.reload(5), 5, msg = message)
        self.assertEqual(Gun_test.reload(7), 7, msg = message)


    def test_shoot_decreases_ammunition(self):
        """--Test ammuniion decreases"""
        message = "Ammunition don't decreases"
        Gun_test.unlock()
        Gun_test.shoot()
        self.assertEqual(Gun_test.get_ammunition, 4, msg = message)
        Gun_test.shoot()
        self.assertEqual(Gun_test.get_ammunition, 3, msg = message)

    def test_shoot_gun_empty(self):
        """--Test if is empty don't shoot """
        message = " Gun shouldn't shoot"
        Gun_test.unlock()
        Gun_test.shoot()
        Gun_test.shoot()
        Gun_test.shoot()
        Gun_test.shoot()


    def test_shoot_gun_locked(self):
        """--Test if is locked don't shoot"""
        message = " Gun shouldn't shoot gun is locked"
        Gun_test.lock()
        Gun_test.reload(3)
        Gun_test.shoot()
        self.assertEqual(Gun_test.get_ammunition, 3, msg = message)




