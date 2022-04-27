"""Special Word Finder: finds random words from a special dictionary with categories of words."""

import random
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Find a random word from a special dictionary"""

    def __init__(self, afile):
        "find a random word from the special dictionary"
        super().__init__(afile)
        self.afile = afile
        self.thefile = open(self.afile, "r")
        self.thelines = self.thefile.readlines()
        self.thefile.close()
        self.qty = len(self.thelines) - 1
        self.uselist = [w.rstrip() for w in self.thelines if w[0] != "#" and len(w.rstrip()) > 0]

    def random(self):
        """ returns a random word from the special dictionary"""
        rline = self.uselist[random.randint(0, len(self.uselist) -1)]
        # print(rline)
        return rline