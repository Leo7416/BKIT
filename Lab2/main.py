from colorama import Fore
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 25.5, 24)
    c = Circle("зеленого", 25)
    s = Square("красного", 25)
    print(r)
    print(c)
    print(s)
    print(Fore.BLUE, r)
    print(Fore.GREEN, c)
    print(Fore.RED, s)
if __name__ == "__main__":
    main()