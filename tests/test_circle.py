from shapes.circle import Circle

def test_perimeter():
    c = Circle()
    c.parse(["Center", "1", "1", "Radius", "2"])
    perimeter = c.get_perimeter()
    assert perimeter == 12.57


