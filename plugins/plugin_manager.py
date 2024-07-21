import importlib
import pkgutil
import os
from .message_plugin import MessagePlugin

class PluginManager:
    def __init__(self, plugin_dir: str):
        self.plugin_dir = plugin_dir
        self.plugins = {}
        self._validate_plugin_dir()

    def _validate_plugin_dir(self):
        if not os.path.isdir(self.plugin_dir):
            raise FileNotFoundError(f"The plugin directory {self.plugin_dir} does not exist.")

    def load_plugins(self):
        for _, module_name, _ in pkgutil.iter_modules([self.plugin_dir]):
            try:
                # Import the module
                module = importlib.import_module(f"{self.plugin_dir}.{module_name}")

                # Iterate through the module attributes
                for attr in dir(module):
                    cls = getattr(module, attr)
                    
                    # Check if the attribute is a subclass of MessagePlugin
                    if isinstance(cls, type) and issubclass(cls, MessagePlugin) and cls is not MessagePlugin:
                        self.plugins[module_name] = cls()
                        print(f"Loaded plugin: {module_name}")
            except Exception as e:
                print(f"Failed to load module {module_name}: {e}")

    def get_plugin(self, plugin_name: str):
        return self.plugins.get(plugin_name)

if __name__ == "__main__":
    # Usage
    plugin_manager = PluginManager('plugins')  # 'plugins' is the directory containing plugin modules
    plugin_manager.load_plugins()

    email_plugin = plugin_manager.get_plugin('email_plugin')
    email_plugin.send("Hello World", "user@example.com")