
def replace(str,old,new):
    result = ""
    for char in str:
        if char == old:
            result = result + new
        else:
            result = result + char
    return result


if __name__ == "__main__":
    res = replace("hell", "l", "L")
    print(res)