from unittest import TestCase
from main import Gun
import sys
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)
        self.gun = Gun(5)

    def tearDown(self):
        pass

    def test_lock(self):
        """-- Test Gun Lock"""
        msg = "The gun is not lock"
        self.assertTrue(self.gun.lock)

    def test_unlock(self):
        pass

    def test_isLock(self):
        pass

    def test_shoot(self):
        pass

    def test_reload(self):
        pass
