#######################################
# Project name: MEB | TrueKey-API     #
# Code&Doc: > github.com/mebofficial  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Official website: > egorik.com      #
# Email: > egorikhelp@gmail.com       #
#######################################

from truekey import TruePort


def main():
    print("#######################################\n"
          "# Project name: MEB | TrueKey-API     #\n"
          "# Code&Doc: > github.com/mebofficial  #\n"
          "# Author's name:    | Link to VK/TG:  #\n"
          "# > Machnev Egor    | > @machnev_egor #\n"
          "# Official website: > egorik.com      #\n"
          "# Email: > egorikhelp@gmail.com       #\n"
          "#######################################\n")

    port = TruePort(input("Seed >>> "))
    while True:
        print(port.get(input("Keyhole >>> ")))


if __name__ == "__main__":
    main()

#######################################
# Project name: MEB | TrueKey-API     #
# Code&Doc: > github.com/mebofficial  #
# Author's name:    | Link to VK/TG:  #
# > Machnev Egor    | > @machnev_egor #
# Official website: > egorik.com      #
# Email: > egorikhelp@gmail.com       #
#######################################
