import sys

# from shapes_classes import Circle, Rectangle, Square
from shapes_classes import Shape

    
def get_shape_classes():
    '''Automatically find all subclasses of Shape'''
    return {
        cls.__name__.lower(): cls
        for cls in Shape.__subclasses__()
    }


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} shape parameters")
        sys.exit(1)
    
    shape_name = sys.argv[1].lower()  # shape name
    params = sys.argv[2:]  # parameters
    
    shape_classes = get_shape_classes()

    try:
        # Check if the shape is supported
        if shape_name not in shape_classes:
            print(f"Error: Unknown shape '{shape_name}'. Supported shapes: {', '.join(shape_classes.keys())}")
            sys.exit(1)

        # Dynamically create an instance of the corresponding shape class
        shape_instance = shape_classes[shape_name]()

        # params parsing:
        shape_instance.parse(params)

        # Generate and print the output
        result = shape_instance.get_output()
        return result

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()