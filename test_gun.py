from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0
print("")


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_correct_craetion(self):
        """-- Testing Correct creation"""
        msg = "Gun created wrong"
        gun = Gun(12)
        self.assertEqual(gun._Gun__cartridge_size, 12, msg=msg)

    def test_reload(self):
        """-- Testing Reload"""
        msg = "Gun reload wrong"
        gun = Gun(12)
        
        returned_bullets = gun.reload("String")
        self.assertEqual(gun._Gun__ammunition, 0, msg=msg)
        self.assertEqual(returned_bullets, "String", msg=msg)

        returned_bullets = gun.reload(-2)
        self.assertEqual(gun._Gun__ammunition, 0, msg=msg)
        self.assertEqual(returned_bullets, None, msg=msg)

        returned_bullets = gun.reload(2)
        self.assertEqual(gun._Gun__ammunition, 2, msg=msg)
        self.assertEqual(returned_bullets, 0, msg=msg)

        returned_bullets = gun.reload(10)
        self.assertEqual(gun._Gun__ammunition, 12, msg=msg)
        self.assertEqual(returned_bullets, 0, msg=msg)

        returned_bullets = gun.reload(10)
        self.assertEqual(gun._Gun__ammunition, 12, msg=msg)
        self.assertEqual(returned_bullets, 10, msg=msg)

    def test_shoot(self):
        """-- Testing Shoot"""
        msg = "The gun shoot wrong"
        gun = Gun(2)
        gun.reload(2)

        gun.shoot()
        self.assertEqual(gun._Gun__ammunition, 1, msg=msg)

        gun.shoot()
        self.assertEqual(gun._Gun__ammunition, 0, msg=msg)

        gun.shoot()
        self.assertEqual(gun._Gun__ammunition, 0, msg=msg)

    def test_lock(self):
        """-- Testing Lock"""
        gun = Gun(12)
        gun.reload(1)

        gun.lock()
        self.assertTrue(gun.is_lock, msg="The gun is not lock")

        gun.shoot()
        self.assertEqual(gun._Gun__ammunition, 1, msg = "The gun can shoot when lock")

        gun.unlock()
        self.assertFalse(gun.is_lock, msg="The gun is not unlock")

        gun.shoot()
        self.assertEqual(gun._Gun__ammunition, 0, msg="The gun can shoot when lock")



