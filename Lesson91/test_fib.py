#Для любого дз (№5) написать набор тестов

import fib

class TestFib:
    def test_0(self):
        assert fib.func(0) == -1
    def test_1(self):
        assert fib.func(1) == 1
    def test_2(self):
        assert fib.func(2) == 1
    def test_3(self):
        assert fib.func(3) == 2
    def test_8(self):
        assert fib.func(8) == 21
    def test_minus_1(self):
        assert fib.func(-1) == -1
    
    