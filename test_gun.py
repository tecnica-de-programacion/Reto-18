from unittest import TestCase
import sys
from main import Gun
sys.tracebacklimit = 0

class TestGun(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_is_Lock(self):
        """-- Test state of Gun isLock"""
        msg = "The Gun doesn't return the correct state of locking"
        gun1 = Gun(20)
        self.assertFalse(gun1.isLock, msg = msg)

    def test_change_of_locking_state(self):
        """-- Test state of Gun when lock is changed"""
        msg = "The Gun doesn't return the correct state of locking when lock is change"
        gun1 = Gun(20)
        gun1.lock()
        self.assertTrue(gun1.isLock, msg = msg)
        gun1.unlock()
        self.assertFalse(gun1.isLock, msg = msg)

    def test_reload_non_numerical(self):
        """-- Test reload with non numerical and float inputs"""
        msg = "Gun can't manage not allowed inputs"
        gun1 = Gun(20)
        self.assertEqual(gun1.reload("hola"),"hola", msg = msg)
        self.assertEqual(gun1.reload(3.25), 3.25, msg=msg)

    def test_reload_negative_integers(self):
        """-- Test reload with negative integers inputs"""
        msg = "Gun can't manage not allowed inputs"
        gun1 = Gun(20)
        self.assertEqual(gun1.reload(-15), None, msg = msg)

    def test_over_reload(self):
        """-- Test realoading more than cartridge capacity"""
        msg = "Gun doesn't return exceeded load"
        gun1 = Gun(5)
        self.assertEqual(gun1.reload(6), 1, msg = msg)

    def test_shooting_when_locked(self):
        """-- Test shooting when Gun is Locked """
        msg = "The Gun doesn't return None when Gun is locked"
        gun1 = Gun(20)
        gun1.lock()
        self.assertEqual(gun1.shoot(),None, msg = msg)

    def test_shooting_without_ammunition(self):
        """-- Test shooting of Gun without ammunition"""
        msg = "The Gun doesn't return None when ammunition is zero"
        gun1 = Gun(20)
        self.assertEqual(gun1.shoot(),None, msg = msg)

    def test_shooting_with_ammunition(self):
        """-- Test shooting of Gun with ammunition """
        msg = "The Gun doesn't shoot correctly"
        gun1 = Gun(20)
        gun1.unlock()
        gun1.reload(5)
        self.assertEqual(gun1.shoot(),4, msg = msg)

