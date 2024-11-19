import math
from abc import ABC, abstractmethod


class Shape(ABC):
    '''Base class for all shapes'''


    @abstractmethod # @abstractmethod means child classes must create their own realization of the methods
    def parse(self, args):
        '''Method for parameters parsing'''
        pass
    
    @abstractmethod
    def get_area(self):
        '''Method for area calculation'''
        pass


    @abstractmethod 
    def get_perimeter(self):
        '''Method for perimeter calculation'''
        pass


    def get_output(self):  # method is ready to use by child classes
        '''Text output creation'''
        area = self.get_area()
        perimeter = self.get_perimeter()
        print(f"{self.__class__.__name__} Perimeter {perimeter} Area {area}")
        return f"{self.__class__.__name__} Perimeter {perimeter} Area {area}"


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
    
    
class Square(Shape):
    

    def __init__(self):
        self.topright = None
        self.side = None 


    def parse(self, args):
        '''Parameters parcing for square'''
        if len(args) != 5 or args[0].lower() != "topright" or args[3].lower() != "side":
            raise ValueError("Invalid format for Square. Expected: 'TopRight X Y Side L'")
        self.topright = (int(args[1]), int(args[2]))
        self.side = int(args[4]) 
        # return {"side": self.side}


    def get_area(self):
        '''Area calculation for square'''
        return self.side**2
    

    def get_perimeter(self):
        '''Perimeter calculation for square'''
        return self.side * 4
    

class Rectangle(Shape):

    def __init__(self):
        self.top_right = None
        self.bottom_left = None


    def parse(self, args):
        '''Parameters parcing for rectangle'''
        if len(args) != 6 or args[0].lower() != "topright" or args[3].lower() != "bottomleft":
            raise ValueError("Invalid format for Rectangle. Expected: 'TopRight X1 Y1 BottomLeft X2 Y2'")
        self.top_right = (int(args[1]), int(args[2]))
        self.bottom_left = (int(args[4]), int(args[5]))
        # return {"top_right": self.top_right, "bottom_left": self.bottom_left}


    def get_area(self):
        '''Area calculation for rectangle'''
        width = abs(self.top_right[0] - self.bottom_left[0])
        lenght = abs(self.top_right[1] - self.bottom_left[1])
        return width * lenght
    

    def get_perimeter(self):
        '''Perimeter calculation for rectangle'''
        width = abs(self.top_right[0] - self.bottom_left[0])
        lenght = abs(self.top_right[1] - self.bottom_left[1])
        perimeter = width * 2 + lenght * 2
        return perimeter
    
