from .base import Shape

# Dynamic import all files in shapes folder (except Base)
import pkgutil
import importlib
import inspect

for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
    # dynamic module import
    module = importlib.import_module(f"{__name__}.{module_name}")
    
    # adding of all child classes of Shape class:
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, Shape) and obj is not Shape:
            globals()[name] = obj
