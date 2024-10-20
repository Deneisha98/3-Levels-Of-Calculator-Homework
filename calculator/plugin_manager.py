import importlib
import pkgutil
from calculator.command import Command

class PluginManager:
    def __init__(self, package):
        self.plugins = {}
        self.package = package

    def load_plugins(self):
        package = importlib.import_module(self.package)
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f"{self.package}.{module_name}")
            for attr in dir(module):
                cls = getattr(module, attr)
                if isinstance(cls, type) and issubclass(cls, Command) and cls is not Command:
                    instance = cls()
                    self.plugins[instance.get_name().lower()] = instance  

    def execute_plugin(self, operation_name, *args):
        """Execute the plugin associated with the operation"""
        operation_name = operation_name.lower()  
        if operation_name not in self.plugins:
            raise ValueError(f"Unknown operation: {operation_name}")
        return self.plugins[operation_name].execute(*args)
