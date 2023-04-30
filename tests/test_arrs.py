import pytest

from utils import arrs


@pytest.fixture
def full_list():
    return [1, 2, 3, 4]


@pytest.fixture
def str_full_list(full_list):
    return [str(i) for i in full_list]


@pytest.fixture
def empty_list():
    return []


def test_get(full_list):
    assert arrs.get(full_list, 1, "test") == 2
    assert arrs.get(full_list, -1, 'test') == 'test'


def test_get_empty_list(empty_list):
    with pytest.raises(IndexError):
        assert arrs.get(empty_list, 0, "test")


def test_get_not_int(full_list):
    with pytest.raises(TypeError):
        assert arrs.get(full_list, '2', "test")


def test_slice(full_list, str_full_list, empty_list):
    assert arrs.my_slice(full_list, 1, 3) == [2, 3]
    assert arrs.my_slice(full_list, 1) == [2, 3, 4]
    assert arrs.my_slice(full_list, -1) == [4]
    assert arrs.my_slice(full_list, 6, 6) == empty_list
    assert arrs.my_slice(full_list, -1, 6) == [4]
    assert arrs.my_slice(full_list) == full_list
    assert arrs.my_slice(full_list, 6, -6) == empty_list
    assert arrs.my_slice(full_list, -6, -6) == empty_list
    assert arrs.my_slice(empty_list, 2, 6) == empty_list
    assert arrs.my_slice(str_full_list, 2, 6) == ['3', '4']


def test_slice_not_int(full_list, str_full_list):
    with pytest.raises(TypeError):
        assert arrs.my_slice(str_full_list, 2, '6')
        assert arrs.my_slice(full_list, '2', 6)
        assert arrs.my_slice(full_list, '2', '6')

