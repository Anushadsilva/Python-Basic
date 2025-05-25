
def factorial(n):
    result = 1
    if n < 0:
        return 1
    for i in range(2,n+1):
        result = result * i

    return result



if __name__ == "__main__":
    result = factorial(5)
    print(result)