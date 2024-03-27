import pytest
import source.shapes as shape

@pytest.fixture
def my_rectange():
    return shape.Rectangle(10, 20)

