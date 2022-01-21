from re import findall
from models.constants import Literals, Constants


class CreateConfig:

    def __init__(self, config):
        self.config = config

    def write_config(self):
        """Write in the config file.

        Args:
            - config (ConfigParser object): configparser object
            - file (str): file name
        """
        with open(Literals.FILE, 'w') as configfile:
            text = ("#################\n"
                    "#  CONFIG FILE  #\n"
                    "#################\n"
                    "\n"
                    "; DO NOT MODIFY [DEFAULT] SECTION\n"
                    "; COPY PASTE WHAT YOU WANT TO MODIFY IN [USER] SECTION\n"
                    "\n")
            configfile.write(text)
            self.config.write(configfile)

    def create_config(self):
        """Create a config file.

        Args:
            - config (ConfigParser object): configparser object
        """
        self.config[Literals.DEFAULT_SECTION] = {
            Literals.PERCENT_UPPERCASE: 0.2,
            Literals.PERCENT_DIGIT: 0.25,
            Literals.PERCENT_PUNCTUATION: 0.2,
            Literals.PUNCTUATION: Constants.PUNCTUATION
        }

        self.config[Literals.USER_SECTION] = {
            Literals.WANTED_PUNCTUATION: [
                '!', '#', '$', '%', '(', ')',
                '*', '-', '.', '/', '@', '_',
            ]
        }

        self.write_config()


class GetConfig:

    def __init__(self, config):

        self.config = config

    def parser(self, string_object):
        """Parse a string containing the punctuation.
        Remove apostrophe and quotation marks

        Args:
            - string_object (str): a string

        Returns:
            - list_caracters (list): a list of caracters
        """
        # regex for caracter between apostrophes
        regex1 = r"\'([^\']*)\'"
        # regex for caracters between quotation marks
        regex2 = r"\"([^\"]*)\""
        # list comprehension with all found elements
        # findall comes from module re
        list_caracters = [elt for regex in [regex1, regex2]
                          for elt in findall(regex, string_object)]

        return list_caracters

    def get_values(self):
        """Get value from the config file

        Returns:
            - dict_config (dict) : a dictionary of values
        """
        dict_config = {}
        for option in self.config.options(Literals.USER_SECTION):
            if option != Literals.PUNCTUATION:
                result = self.config.get(Literals.USER_SECTION, option)
                if option == Literals.WANTED_PUNCTUATION:
                    result = self.parser(result)
                    dict_config[option] = [
                        elt for elt in Constants.PUNCTUATION
                        if elt in result
                    ]
                else:
                    dict_config[option] = self.config.getfloat(
                        Literals.USER_SECTION, option)
        return dict_config


class ConfigFileValidation:

    def __init__(self, config):
        self.config = config
        self.options = None
        self.test_result = True

    def get_options(self, section):
        """Get options name of the user section"""

        # config._sections["section"] return a dict of the section
        self.options = self.config._sections[section].keys()

    def is_float(self, option):
        """Verify if the option is a float.

        Args:
            - option : option form the cofig file

        Returns:
            - a boolean
        """
        try:
            self.config.getfloat(Literals.USER_SECTION, option)
        except ValueError:
            print(f"Invalid value for '{option} : "
                  f"{self.config.get(Literals.USER_SECTION, option)}'\n"
                   "Option must be a number between 0 and 1")
            return False
        return True

    def value_validation(self):
        """Verify if each value in USER section is a float.
        If not set self.test_result to False."""
        for option in self.options:
            if option != Literals.WANTED_PUNCTUATION:
                result = self.is_float(option)
                if not result:
                    self.test_result = False
                    break

    def verify_interval(self, value, lower, upper):
        """Verify if a value is in the interval [lower, upper]

        Args:
            - value : a number
            - lower : the lower bound
            - upper : the upper bound

        Returns:
            - a boolean
        """
        if value < lower or value > upper:
            return False
        return True

    def interval_validation(self):
        """Verify if each value in USER section is in the interval.
        If not set self.test_result to False"""
        for option in self.options:
            if option != Literals.WANTED_PUNCTUATION:
                value = self.config.getfloat(Literals.USER_SECTION, option)
                result = self.verify_interval(value, 0, 1)
                if not result:
                    self.test_result = False
                    print(f"Invalid value for '{option} : "
                          f"{self.config.get(Literals.USER_SECTION, option)}"
                           "'\n"
                           "Value can't be lower to 0 or upper to 1")
                    break

    def sum_validation(self):
        """Verify if the sum of each value in USER section is lower to 1.
        If not set self.test_result to False"""
        sum_percentage = 0
        for option in self.options:
            if option != Literals.WANTED_PUNCTUATION:
                sum_percentage += self.config.getfloat(Literals.USER_SECTION,
                                                       option)
                if sum_percentage > 1:
                    self.test_result = False
                    print('The sum of percentage must be lower or equal to 1')
                    break

    def run_validation(self):
        """Run the each validation of the config file"""
        self.get_options(Literals.USER_SECTION)
        functions = [self.value_validation, self.interval_validation,
                     self.sum_validation]
        for function in functions:
            function()
            if not self.test_result:
                print('All values in config file have been set to default')
                break
