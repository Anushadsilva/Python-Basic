import math
def upper(str):
    str1 = str.upper()
    print(str1)

def radius(r):
    area = math.pi * r * r
    return area


if __name__ == "__main__":
    upper("abc")
    area = radius(20)
    print(area)
