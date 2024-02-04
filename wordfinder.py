"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Read the file and reports the number of words read."""
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

    def read_words(self, filepath):
        """Read the file and return a list of words."""
        with open(filepath) as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""

    def read_words(self, filepath):
        """Read the file and return a list of words, skipping blanks/comments."""
        with open(filepath) as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
