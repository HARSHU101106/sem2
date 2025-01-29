sentence = input()
words = sentence.split()
longest_word = max(words, key=len)
print(longest_word, len(longest_word))
