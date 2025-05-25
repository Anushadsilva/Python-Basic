def largest(a,b,c):
    largest = a
    if b > a and b > c:
        largest = b
    elif c > a and c > b:
        largest = c

    return largest





if __name__ == "__main__":
    largest = largest(5,5,4)
    print(largest)