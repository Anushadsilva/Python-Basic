def sumofnums(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

if __name__ == "__main__":
    result = sumofnums(5)
    print(result)