import random
import os
from models.constants import Literals, Constants


class RandomPassword:
    def __init__(self, number_of_characters, values):
        self.number_of_characters = number_of_characters
        self.values = values
        self.occurences = {}
        self._set_percent_lowercase()
        self._set_occurences()

    @property
    def _characters_and_occurences(self):
        return [
            (Constants.ALPHABET_LOWERCASE, 
                self.occurences['occurence_lowercase']),
            (Constants.ALPHABET_UPPERCASE,
                self.occurences['occurence_uppercase']),
            (Constants.DIGIT,
                self.occurences['occurence_digit']),
            (self.values[Literals.WANTED_PUNCTUATION],
                self.occurences['occurence_punctuation'])
        ]

    def _get_number_of_occurence(self, percentage):
        """Returns the number of occurence"""
        return int(self.number_of_characters * percentage)

    def _set_percent_lowercase(self):
        """Set percent lowercase"""
        self.values[Literals.PERCENT_LOWERCASE] = (
            1 - self.values[Literals.PERCENT_PUNCTUATION]
              - self.values[Literals.PERCENT_DIGIT]
              - self.values[Literals.PERCENT_UPPERCASE]
        )

    def _set_occurences(self):
        """Set the number of occurence for each percentage"""
        for key, value in self.values.items():
            if key != Literals.WANTED_PUNCTUATION:
                name = key.replace('percent', 'occurence')
                occurence = self._get_number_of_occurence(value)
                self.occurences[name] = occurence

    def _adjust_occurences(self):
        """Adjust the number of occurence"""
        sum_occurence = 0
        for key, value in self.occurences.items():
            sum_occurence += value
        if sum_occurence != self.number_of_characters:
            difference = self.number_of_characters - sum_occurence
            self.occurences['occurence_lowercase'] += difference

    def _get_random(self, list, number_of_occurences):
        """Takes random elements from a list

        Args:
            - list (list): a complete list of caracters
            - number_of_occurences (int): the number of elements we want

        Returns:
            - a list (list) of randomly choosen elements
        """

        return random.choices(list, k=number_of_occurences)

    def create_password(self):
        """Creates a random passaword"""
        self._adjust_occurences()
        characters_and_occurences = self._characters_and_occurences
        list_of_characters = []
        for characters, occurence in characters_and_occurences:
            list_of_characters.extend(self._get_random(characters, occurence))

        random.shuffle(list_of_characters)
        password = "".join(list_of_characters)

        return password
