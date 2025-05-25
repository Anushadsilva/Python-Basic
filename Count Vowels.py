
def count_vowel(str):
    count = 0
    vowel = 'aeiouAEIOU'
    for char in str:
        if char in vowel:
            count += 1
    print("Is a vowel", count)


if __name__ == "__main__":
    count = count_vowel("aerofix")
