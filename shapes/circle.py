import math
from .base import Shape


class Circle(Shape):


    def __init__(self):
        self.center = None # place to save center coordinates
        self.radius = None # place to save radius


    def parse(self, args):
        '''Parameters parcing for circle'''
        if len(args) != 5 or args[0].lower() != "center" or args[3].lower() != "radius":
            raise ValueError("Invalid format for Circle. Expected: 'Center X Y Radius R'")
        self.center = (int(args[1]), int(args[2]))
        self.radius = int(args[4])
        # return {"radius": self.radius}

    
    def get_area(self): # S = πr^2
        '''Area calculation for circle'''
        area = round((math.pi * self.radius ** 2), 2)
        return area
    

    def get_perimeter(self): #  C = 2πr
        '''Perimeter calculation for circle'''
        perimeter = round((2 * math.pi * self.radius), 2)
        return perimeter