def main():
    cases = int(input())
    for i in range(1, cases + 1):
        string = list(input())
        string.reverse()
        words = []
        # While there are letters to grab from the string
        while string:
            letter = string.pop()
            if words:
                new_words = []
                while words:
                    word = words.pop()
                    # Selectively picks where the letter should go and reduces the amount of words stored
                    if word[0] > letter:
                        new_words.append("{word}{letter}".format(**locals()))
                    else:
                        new_words.append("{letter}{word}".format(**locals()))
                words.extend(new_words)
            else:
                words.append(letter)
        words.sort()
        print("Case #{i}: {}".format(words.pop(), **locals()))


if __name__ == '__main__':
    main()
