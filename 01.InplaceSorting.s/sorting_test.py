"""
Unit tests for 00.Demo
"""

import random
import pytest
from comp_swap_container import CompSwapList
import sortings


@pytest.fixture()
def fatal_array():
    """
    Create a shuffled array of 1000 elements with fixed seed
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield CompSwapList(data)


def test_trivial_sort2():
    """
    Test trivial sorting of a 2-element array
    """
    a2: CompSwapList[int] = CompSwapList([2, 1])
    sortings.trivial_sort2(a2)
    assert list(a2) == [1, 2]


@pytest.mark.parametrize(
    "sort_func",
    [
        sortings.bubble_sort,
        sortings.quick_sort,
    ],
)
def test_some_sorting(sort_func, fatal_array):
    """
    Test some sorting algorithm
    """
    # replace with a call to a sorting algorithm
    # that uses `less` and `swap`
    sort_func(fatal_array)

    assert list(fatal_array) == sorted(fatal_array)


@pytest.mark.parametrize("size", [0, 1, 10, 100, 1000])
def test_sorting_diff_size(size):
    data = list(range(size))
    random.shuffle(data)
    arr = CompSwapList(data)
    sortings.quick_sort(arr)

    assert list(arr) == sorted(data)


def test_empty_array():
    arr = CompSwapList([])
    sortings.quick_sort(arr)

    assert list(arr) == []


def test_one_element():
    arr = CompSwapList([1])
    sortings.quick_sort(arr)

    assert list(arr) == [1]


def test_sorted_array():
    arr = CompSwapList([1, 2, 3, 4, 5])
    sortings.quick_sort(arr)

    assert list(arr) == [1, 2, 3, 4, 5]


def test_big_sorted_array():
    data = list(range(1000))

    arr = CompSwapList(data)

    sortings.quick_sort(arr)

    assert list(arr) == data
