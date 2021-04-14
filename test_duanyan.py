import pytest

def su(a,b):
    n = a + b
    return n

def test_1():
    ss = su(1,2)
    assert 3 == ss

def test_2():
    ss = su(-1,2)
    assert 1 == ss

def test_3():
    ss = su(1,-2)
    assert -1 == ss

def test_4():
    ss = su(-1,-2)
    assert -3 == ss

#参数化使用

# @pytest.mark.parametrize("a,b,ss",[
#     (1,3,4),(-2,-3,-5),(-1,6,5)
# ])
# def test_add(a,b,ss):
#     assert sum(a,b) == ss

#参数化 加别名

@pytest.mark.parametrize("a,b,ss",[
    (1,3,4),(-2,-3,-5),(-1,6,5) # 这部分会 pass
    # (1,1,3) #这是一个错误测试run 之后会failed
    ],
    ids = ["int1","int2","sumint"]
)
class Test_add():
    def test_add(self,a,b,ss):
        assert su(a,b) == ss
    
