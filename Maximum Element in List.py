


def maximum(lst):
    max = lst[0]
    for num in lst[1:]:
        if num > max:
            max = num
    return max


if __name__ == "__main__":
    max = maximum([5,7,3,2,1])
    print(max)