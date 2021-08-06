#######################################
# Project name: MEB | TrueKey-API     #
# Code&Doc: > github.com/mebofficial  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Official website: > egorik.com      #
# Email: > egorikhelp@gmail.com       #
#######################################

from random import random
from hashlib import md5


class TruePort():
    """
    Description
    -----------
    This class allows you to get keys from the source seed
    and the keyhole for this key.

    Methods
    -------
    get(self, keyhole: str, length: int = 30)
    """

    def __init__(self, seed: str = ""):
        """
        Expects
        -------
        :param seed: (str, optional)
            Seed for further obtaining key hashes.
        """

        self.seed = seed if seed != "" else str(random())[2:]

    def __repr__(self):
        """
        Description
        -----------
        Method that outputs information about an instance
        of the class.
        """

        return f"<TruePort seed={self.seed}>"

    def get(self, keyhole: str, length: int = 30):
        """
        Description
        -----------
        This method, using the hashlib library and simple
        transformations, allows you to get a hashed key.

        Expects
        -------
        :param seed: (str, optional)
            The keyhole for which the key will be obtained.
        :param length: (int, optional)
            The length of the key that should result in.

        Returns
        -------
        Returns the hashed key obtained by merging the
        initial seed and keyhole.
        """

        key = md5(("".join([str(ord(letter)) for letter in keyhole]) + "".join(
            [str(ord(letter)) for letter in self.seed])).encode()).hexdigest()

        for letter in key:
            if key.count(letter) % 2 == 0:
                key = key.replace(letter, letter.upper())

        return key[:length] if length < len(key) else key
