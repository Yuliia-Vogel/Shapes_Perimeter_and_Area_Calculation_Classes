from .base import Shape


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