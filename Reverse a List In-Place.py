


def reverse(st):
    if len(st) <= 0:
        return False

    left = 0
    right = len(st) -1

    while left < right:
        st[left] , st[right] = st[right], st[left]
        left += 1
        right -= 1
    print(st)


if __name__ == "__main__":
    reverse([2 ,3 ,5])