#Реализовать любое из предыдущих дз (№3) с применением подхода
#разработки TDD, т.е. сначала пишем необходимые тесты, а затем
#пишем код для прохождения этих тестов

import func_equation as f

class TestEq:
    def test_1_4_4(self):
        assert f.func(1, 4, 4) == [-2.0]
    def test_0_8_4(self):
        assert f.func(0, 8, 4) == [-0.5]
    def test_1_5_6(self):
        assert f.func(1, 5, 6) == [-2.0, -3.0]
    def test_1_5_20(self):
        assert f.func(1, 5, 20) == 0
    def test_0_0_0(self):
        assert f.func(0, 0, 0) == 1
    def test_0_0_1(self):
        assert f.func(0, 0, 1) == 0
    def test_0_2_0(self):
        assert f.func(0, 2, 0) == [0]