#######################################
# Project name: MEB | TrueKey-API     #
# Official website: > kostyl.net      #
# Code&Doc: > github.com/machnevegor  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Email: > meb.official.com@gmail.com #
#######################################

from time import sleep
from truekey import TruePort

LOADING_TEXT = "\n".join([
    "#######################################",
    "# Project name: MEB | TrueKey-API     #",
    "# Official website: > kostyl.net      #",
    "# Code&Doc: > github.com/machnevegor  #",
    "# Author's name:    | Link to VK/TG:  #",
    "# > Machnev Egor    | > @machnev_egor #",
    "# Email: > meb.official.com@gmail.com #",
    "#######################################"
])


def typewriter(text: str, time: int):
    for line in text.split("\n"):
        for letter in line:
            print(letter, end='', flush=True)
            sleep(time / len(text) / len(line))
        print()


if __name__ == "__main__":
    typewriter(text=LOADING_TEXT, time=3)
    print()
    typewriter(text="So, first, enter seed to generate the encrypted key:", time=1)
    generator = TruePort(seed=str(input(">>> ")))
    typewriter(text="Now enter the keyhole for which the key will be intended:", time=1)
    key = generator.create(keyhole=str(input(">>> ")))
    typewriter(text="Great, here's your new encrypted key:", time=1)
    typewriter(text=f">>> {key}", time=1)

#######################################
# Project name: MEB | TrueKey-API     #
# Official website: > kostyl.net      #
# Code&Doc: > github.com/machnevegor  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Email: > meb.official.com@gmail.com #
#######################################
