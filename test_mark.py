import pytest

class Test_Demo2():
    @pytest.mark.demo
    def tst_demo(self):
        a = 5
        b = -1
        assert a !=b
        print("这是demo标签")

    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b = -1
        assert a!=b
        print("这是somke标签")
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @pytest.mark.demo
    def test_three(self):
        a = 2
        b = -1
        assert a!=b
        print("这是somke标签")
