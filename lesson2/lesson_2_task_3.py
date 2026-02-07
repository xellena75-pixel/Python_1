import math
def square(side):
    area = side ** 2
    return math.ceil(area)
if __name__ == "__main__":
    print(square(5))
    print(square(5.5))  