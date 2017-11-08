from unittest import TestCase
from main import Gun
import sys

sys.tracebacklimit = 0


class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def test_lock_gun(self):
        '''Test Locked Gun'''
        msg = 'The correct value is not the expected'
        self.assertEqual(Gun.lock(self), None, msg = msg)
        self.assertEqual(Gun.lock(self), True, msg=msg)
    
