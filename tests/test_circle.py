import pytest

from shapes.circle import Circle


@pytest.fixture
def circle():
    c = Circle() # фікстура
    c.parse(["Center", "1", "1", "Radius", "3"])
    return c


def test_perimeter(circle):
    perimeter = circle.get_perimeter()
    assert perimeter == 18.85


def test_area(circle):
    area = circle.get_area()
    assert area == 28.27