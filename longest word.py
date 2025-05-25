

def longest(sentence):
    word = sentence.split()
    max_length = 0
    for word in word:
        if len(word) >= max_length:
            max_length = len(word)
    return max_length, word


if __name__ == "__main__":
    word,max_length = longest( "Hi My name is Bestest")
    print(word,max_length)