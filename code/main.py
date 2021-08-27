#########################################
# Project name: MEB | TrueKey-API [1.2] #
# Code&Doc: > github.com/machnevegor    #
# Author's name:    | Link to VK/TG:    #
# > Machnev Egor    | > @machnev_egor   #
# Email: > egorikhelp@gmail.com         #
#########################################

from truekey import TruePort


def main():
    print("#########################################\n"
          "# Project name: MEB | TrueKey-API [1.2] #\n"
          "# Code&Doc: > github.com/machnevegor    #\n"
          "# Author's name:    | Link to VK/TG:    #\n"
          "# > Machnev Egor    | > @machnev_egor   #\n"
          "# Email: > egorikhelp@gmail.com         #\n"
          "#########################################\n")

    port = TruePort(input("Seed >>> "))
    while True:
        print(port.get(input("Keyhole >>> ")))


if __name__ == "__main__":
    main()

#########################################
# Project name: MEB | TrueKey-API [1.2] #
# Code&Doc: > github.com/machnevegor    #
# Author's name:    | Link to VK/TG:    #
# > Machnev Egor    | > @machnev_egor   #
# Email: > egorikhelp@gmail.com         #
#########################################
