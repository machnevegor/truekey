#######################################
# Project name: MEB | TrueKey-API     #
# Official website: > kostyl.net      #
# Code&Doc: > github.com/machnevegor  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Email: > meb.official.com@gmail.com #
#######################################

from random import getrandbits
from hashlib import md5


class TruePort():
    """
    Description
    -----------
    This class allows you to get hashes for keyholes by seeds.

    Methods
    -------
    create(self, keyhole: str)
    """

    def __init__(self, seed: str = "%x" % getrandbits(256)):
        """
        Expects
        -------
        :param seed: (str, optional)
            Seed for further key hashing.
        """

        self.seed = seed

    def create(self, keyhole: str = "%x" % getrandbits(256)):
        """
        Description
        -----------
        This method, using the hashlib library and simple transformations, allows you to get a hashed key.

        Expects
        -------
        :param seed: (str, optional)
            The keyhole for which the key will be created.

        Returns
        -------
        Returns a hashed key created by merging seed and keyhole.
        """

        # generating a hashed key by multiplying two arrays with the seed and keyhole character codes
        key = md5("".join(list(map(lambda keyhole, seed: str(keyhole * seed), [ord(letter) for letter in keyhole],
                                       [ord(letter) for letter in self.seed]))).encode()).hexdigest()

        # creating capital letters by analyzing the number of letter occurrences in a key
        for letter in key:
            if key.count(letter) % 2 == 0:
                key = key.replace(letter, letter.upper())

        # returning a truncated key to 24 characters in accordance with key security standards
        return key[:24]

#######################################
# Project name: MEB | TrueKey-API     #
# Official website: > kostyl.net      #
# Code&Doc: > github.com/machnevegor  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Email: > meb.official.com@gmail.com #
#######################################
