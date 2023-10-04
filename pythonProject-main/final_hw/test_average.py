import pytest
from average_list import AverageList


def test1_find_average():
    assert AverageList.findaverage([10, 20, 30, 40, 50]) == 30


def test2_find_average():
    assert AverageList.findaverage([]) is None


def test3_find_average():
    assert AverageList.findaverage([3]) == 3


def test4_find_average():
    with pytest.raises(TypeError):
        AverageList.findaverage("string")


def test1_list_comparison():
    assert AverageList.list_comparison([3, 5, 7], [3, 6, 2]) == \
           "Первый список имеет большее среднее значение"


def test2_list_comparison():
    assert AverageList.list_comparison([3, 5, 7], [3, 6, 20]) == \
           "Второй список имеет большее среднее значение"


def test3_list_comparison():
    assert AverageList.list_comparison([3, 5, 7], [3, 5, 7]) == "Средние значения равны"


def test4_list_comparison():
    with pytest.raises(TypeError):
        AverageList.list_comparison("ls", [3, 5, 7])


def test5_list_comparison():
    with pytest.raises(TypeError):
        AverageList.list_comparison([3, 5, 7], "ls")


def test6_list_comparison():
    with pytest.raises(TypeError):
        AverageList.list_comparison("ls", "ls")


def test7_list_comparison():
    assert AverageList.list_comparison([], [3, 5, 7]) is None


def test8_list_comparison():
    assert AverageList.list_comparison([3, 5, 7], []) is None


def test9_list_comparison():
    assert AverageList.list_comparison([], []) is None


