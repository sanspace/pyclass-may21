import pytest

def add(x,y):
    return x + y

@pytest.mark.parametrize(
    'input1,input2,result', [
        (2,3,5),
        (1,2,3),
        ("s", "k", "sk"),
        ([1],[2],[1,2])
])
def test_add(input1, input2, result):
    assert add(input1, input2) == result