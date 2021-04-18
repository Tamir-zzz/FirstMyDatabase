import pytest
@pytest.fixture()
def myfixture():
    print("执⾏myfixture")
class Test_firstFile():
    def test_one(self):
        print("执⾏test_one")
        assert 2++3==5
    def test_two(self,myfixture):
        print("执⾏test_two")
        assert 1==1
    def test_three(self):
        print("执⾏test_three")

