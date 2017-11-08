from unittest import TestCase
from main import Gun
import sys

sys.tracebacklimit = 0


class TestGun(TestCase):
    msg = 'The value doesnt correspond'
    def setUp(self):
        print(self._testMethodDoc)

    def test_lock_gun(self):
        '''Test Locked Gun'''
        self.assertEqual(Gun.lock(self), None, msg = self.msg)

    def test_unlock_gun(self):
        '''Test Unlocked Gun'''
        self.assertEqual(Gun.unlock(self), None, msg=self.msg)

    def test_shoot(self):
        '''Test Shoot'''
        if Gun.isLock == bool:
            self.assertIsNone(Gun.shoot(self), msg=self.msg)

    def test_reload(self):
        '''Test Shoot'''
        self.assertEqual(Gun.reload(self, int), int, msg = self.msg)

