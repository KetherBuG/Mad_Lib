


class Menu:
    def __init__(self):
        self.options = {
            0:["Start"],
            1:["Quit"]
        }
        self.begin = 0
        self.end = 1


def menu():

    print("=" * 25)
    print("Welcome to Mad lab")
    print("=" * 25)
    print("")
    print("1. Start\n")
    print("2. Quit\n")
    option = input("Select Option: ")

    optionSelect(option)

class selections(object):
    def one(self):
        print("option one")

    def two(self):
        print("option two")

    def three(self):
        print("option three")

    def four(self):
        print("option four")

def optionSelect(test):
    menuSelection = selections()
    optionMenu = {
        1: menuSelection.one,
        2: menuSelection.two,
        3: menuSelection.three,
        4: menuSelection.four,
    }

    func = optionMenu.get(test)
    if test in optionMenu:
        func()
    else:
        print("ERROR INVALID ENTRY ERROR")