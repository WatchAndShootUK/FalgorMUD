import importlib
import os

items = {}

class LoadItems:
    def __init__(self):
        directory = 'areas/towns/bree/obj'
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    spec = importlib.util.spec_from_file_location(file, full_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name in dir(module):
                        obj = getattr(module, name)
                        if hasattr(obj, '__class__') and obj.__class__.__name__ == 'type' and name == 'ThisItem':
                            thisItem = obj()
                            items[thisItem.short] = thisItem