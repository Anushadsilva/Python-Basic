
import math
def squareroot(num):
    res = math.sqrt(num)
    return res

def powerofnum(base,expo):
    result = 1
    for _ in range(int(expo)):
        result = result * base
    return result




if __name__ == "__main__":
    res = squareroot(255)
    print(res)


    result = powerofnum(3, 2)
    print(result)


