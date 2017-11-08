from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    gun = Gun(3)

    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_status_of_the_gun(self):
        """ Test Status of the Gun """
        msg = "The correct status is not being returned"
        self.gun.lock()
        self.assertEqual(self.gun.isLock, True, msg = msg)
        self.gun.unlock()
        self.assertEqual(self.gun.isLock, False, msg=msg)

    def test_reload(self):
        """ Test reload """
        msg = " does not recharge the weapon "
        self.gun.reload(3)
        self.assertEqual(self.gun.bullets, 3, msg = msg)

    def test_one_bullet_per_shot(self):
        """ Test one bullet per shot """
        msg = "does not eliminate one bullet per shot"
        self.gun.reload(3)
        self.gun.shoot()
        self.assertEqual(self.gun.bullets, 2, msg=msg)
        self.gun.shoot()
        self.assertEqual(self.gun.bullets, 1, msg=msg)
        self.gun.shoot()
        self.assertEqual(self.gun.bullets, 0, msg=msg)

