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

# the text that will be displayed at the start of the program
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


# a function that creates the effect of step-by-step text pri
def typewriter(text: str, time: int):
    for line in text.split("\n"):
        for letter in line:
            print(letter, end='', flush=True)
            sleep(time / len(text) / len(line))
        print()


# the main code of the program that interacts with the API
if __name__ == "__main__":
    # output of a special text at the start of the program
    typewriter(text=LOADING_TEXT, time=3)

    # create an indent for further more enjoyable interaction
    print()

    # generating a hashed key using the imported API
    typewriter(text="So, first, enter seed to generate the encrypted key:", time=1)
    seed = str(input(">>> "))
    generator = TruePort(seed=seed) if seed != "" else TruePort()
    typewriter(text="Now enter the keyhole for which the key will be intended:", time=1)
    keyhole = str(input(">>> "))
    key = generator.create(keyhole=keyhole) if seed != "" else generator.create()
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
