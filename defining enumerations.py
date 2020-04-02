
from enum import Enum



class fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4


def main():
    pass

    print (fruit.APPLE)
    print (type(fruit.APPLE))
    print (repr(fruit.APPLE))




if __name__ == "__main__":
    main()