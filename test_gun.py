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
