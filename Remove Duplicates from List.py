def dup(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    print(new_list)


if __name__ == "__main__":
    dup([6,8,9,8,5,3,6])