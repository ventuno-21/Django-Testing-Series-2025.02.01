import pytest


def raise_my_exception():
    raise ValueError("My personal exception!")


def test_raise_my_exception_which_should_pass():
    with pytest.raises(ValueError) as e:
        raise_my_exception()
    assert "My personal exception!" == str(e.value)
