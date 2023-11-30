"""
Question 10
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
"""
words = input('input some words whitespace-separated: ').split()
words_set = set(words)
words_set = sorted(words_set)
print(' '.join(words_set))

# standard anwsers
word = sorted(list(set(input('input some words whitespace-separated: ').split())))
print(' '.join(word))

# standard anwsers
words = input('input some words whitespace-separated: ').split()
for word in words:
    if words.count(word) > 1:
        words.remove(word)
words.sort()
print(' '.join(words))
