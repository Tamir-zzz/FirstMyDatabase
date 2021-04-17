import pytest
import yaml

def add_fun(a,b):
    return a+b
@pytest.mark.parametrize("a,b,exp",
                yaml.safe_load(open("ceshi/datas.yml"))["datas"],
                ids = yaml.safe_load(open("ceshi/datas.yml"))["myid"]
                )

def test_add(a,b,exp):
    assert add_fun(a,b) == exp

def get_datas():
    with open("ceshi/datas.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return [add_datas,add_ids]
@pytest.mark.parametrize("a,b,exp",
                get_datas()[0],
                ids = get_datas()[1]
                )

def test_add1(a,b,exp):
    assert add_fun(a,b) == exp


#datas.yml
# datas:
#  -
#   - 3
#   - 5
#   - 8
#  -
#   - -1
#   - -2
#   - -3
#  -
#   - 100
#   - 200
#   - 300
# myid:
#  - "int"
#  - "minus"
#  - "bigint"

