import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3, 4], -1, 'test') == 'test'


def test_get_empty_list():
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test")


def test_get_not_int():
    with pytest.raises(TypeError):
        assert arrs.get([1, 2, 3], '2', "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3, 4], 6, 6) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, 6) == [4]
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 6, -6) == []
    assert arrs.my_slice([1, 2, 3, 4], -6, -6) == []
    assert arrs.my_slice([], 2, 6) == []
    assert arrs.my_slice(['1', '2', '3'], 2, 6) == ['3']


def test_slice_not_int():
    with pytest.raises(TypeError):
        assert arrs.my_slice(['1', '2', '3'], 2, '6')
        assert arrs.my_slice([1, 2, 3], '2', 6)
        assert arrs.my_slice([1, 2, 3], '2', '6')

