
def palin(st):
    if len(st) <= 0:
        return False
    left = 0
    right = len(st) - 1
    while left < right:
        if st[left] != st[right]:
            print("Is not Palindrome")
            return False
        left += 1
        right -= 1
    print("Is Palindrome")
    return True


if __name__ == "__main__":
    palin("daada")