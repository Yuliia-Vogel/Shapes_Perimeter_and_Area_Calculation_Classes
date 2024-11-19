from .base import Shape


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
    
