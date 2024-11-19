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