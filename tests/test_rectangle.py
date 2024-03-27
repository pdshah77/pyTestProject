import pytest
import source.shapes as shape

def test_area(my_rectange):
    assert my_rectange.area() == 10 * 20


def test_perimeter(my_rectange):
    assert my_rectange.perimeter() == (10 * 2) + (20 * 2)

