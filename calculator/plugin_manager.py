# calculator/plugin_manager.py
import importlib
import pkgutil
from calculator.command import Command

class PluginManager:
    def __init__(self, package):
        self.plugins = {}
        self.package = package

    def load_plugins(self):
        # Discover and load all modules in the specified package
        package = importlib.import_module(self.package)
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            # Import the module
            module = importlib.import_module(f"{self.package}.{module_name}")
            # Register each command class found in the module
            for attr in dir(module):
                cls = getattr(module, attr)
                if isinstance(cls, type) and issubclass(cls, Command) and cls is not Command:
                    instance = cls()
                    self.plugins[instance.get_name()] = instance

    def execute_plugin(self, name, *args):
        # Execute the desired plugin by name
        plugin = self.plugins.get(name)
        if plugin:
            return plugin.execute(*args)
        else:
            raise ValueError(f"Plugin '{name}' not found")
