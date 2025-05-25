
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            print("Not anagrams")
            return False
        count[char] -= 1
    print("Anagrams")





if __name__ == "__main__":
    anagram("silentcsw", "lentsicss")