import yaml

from plugins.plugin_manager import PluginManager

def load_config(config_file: str):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

config = load_config('config.yaml')

plugin_manager = PluginManager('plugins')
plugin_manager.load_plugins()

for plugin_name in config['plugins']:
    plugin = plugin_manager.get_plugin(plugin_name)

    if plugin:
        plugin.send("Hello World", "user@example.com")