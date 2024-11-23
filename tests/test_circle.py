from shapes.circle import Circle

def test_perimeter():
    c = Circle()
    c.parse(["Center", "1", "1", "Radius", "3"])
    perimeter = c.get_perimeter()
    assert perimeter == 18.85


def test_area():
    c = Circle()
    c.parse(["Center", "1", "1", "Radius", "3"])
    area = c.get_area()
    assert area == 28.27