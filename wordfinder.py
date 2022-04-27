"""Word Finder: finds random words from a dictionary.

        
    >>> random.seed(1)

    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.random()
    'choler'


"""

import random

class WordFinder:
    """Find a random word from a dictionary"""

    def __init__(self, afile):
        "find a random word from the dictionary"
        self.afile = afile
        self.thefile = open(self.afile, "r")
        self.thelines = self.thefile.readlines()
        self.thefile.close()
        print(f"{len(self.thelines)} words read")
        self.qty = len(self.thelines) - 1
    
    def random(self):
        """ returns a random word from the dictionary"""
        rline = self.thelines[random.randint(0, self.qty)]
        # return print(rline.rstrip())
        return rline.rstrip()
        # return rline


    