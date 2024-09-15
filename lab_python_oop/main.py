from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

def main():
    r = Rectangle("синего", 3, 3)
    c = Circle("зеленого", 3)
    s = Square("красного", 3)
    arr = np.array([r, c, s])
    print(*arr, sep='\n')
    print()
    print("Вот и numpy:")
    arr2 = np.array([Rectangle("фиолетового", 3, 4), Rectangle("красного", 5, 7)])
    arr3 = np.array([Square("зеленого", 9), Circle("черного", 2)])
    big_arr = np.concatenate((arr, arr2, arr3))
    print(*big_arr, sep='\n')

if __name__ == "__main__":
    main()