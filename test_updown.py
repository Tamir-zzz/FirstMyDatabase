import pytest
# 模块中的⽅法
def setup_module():
    print(
        "\nsetup_module：整个test_module.py模块只执⾏⼀次"
    )
def teardown_module():
    print(
    "\nteardown_module：整个test_module.py模块只执⾏⼀次"
    )
def setup_function():
    print("\nsetup_function：每个不在类中的⽤例开始前都会执⾏")
def teardown_function():
    print("\nteardown_function：每个不在类中的⽤例结束后都会执⾏")
# 测试模块中的⽤例1
def test_one():
    print("正在执⾏测试模块--test_one")

# 测试类
class TestCase():
    def setup_class(self):
        print("\nsetup_class：所有⽤例执⾏之前")
    def teardown_class(self):
        print("\nteardown_class：所有⽤例执⾏之后")


    def setup_method(self):
        print("\nsetup_method: 每个⽤例开始前执⾏")
    def teardown_method(self):
        print("\nteardown_method: 每个⽤例结束后执⾏")


    def setup(self):
        print("\nsetup：每个⽤例开始前都会执⾏")
    def teardown(self):
        print("\nteardown：每个⽤例结束后都会执⾏")

    def test_two(self):
        print("\n正在执⾏测试类----test_three")

