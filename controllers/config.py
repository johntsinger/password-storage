from configparser import ConfigParser
from models.config import CreateConfig, ConfigFileValidation, GetConfig
from models.constants import Literals


class ConfigController:

    def __init__(self):
        self.config = ConfigParser(interpolation=None)
        self.create_config = CreateConfig(self.config)
        self.validation = ConfigFileValidation(self.config)
        self.get_config = GetConfig(self.config)
        self.values = {}

    def config_file_exists(self):
        """Verify if the config file exists.
        Otherwise create it."""
        try:
            with open(Literals.FILE):
                pass
        except IOError:
            self.create_config.create_config()

    def run(self):
        self.config_file_exists()
        self.config.read(Literals.FILE)
        self.validation.run_validation()
        if not self.validation.test_result:
            self.create_config.create_config()
            self.validation.test_result = True
        self.values = self.get_config.get_values()
