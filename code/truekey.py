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

        key = md5(str(keyhole + self.seed).encode()).hexdigest()
        for letter in key:
            if key.count(letter) % 2 == 0:
                key = key.replace(letter, letter.upper())
        return key[:24]

#######################################
# Project name: MEB | TrueKey-API     #
# Official website: > kostyl.net      #
# Code&Doc: > github.com/machnevegor  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Email: > meb.official.com@gmail.com #
#######################################
