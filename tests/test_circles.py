import pytest
import math
import source.shapes as shape


class TestCircle:

    def setup_method(self):
        print("Setting up Radius Value")
        self.circle = shape.Circle(3)

    def test_circle_area(self):
        assert self.circle.area() == math.pi*self.circle.radius ** 2

    def test_circle_perimeter(self):
        assert self.circle.perimeter() == math.pi*2*self.circle.radius

    def teardown_method(self):
        print("Tear down Method")
        del self.circle



