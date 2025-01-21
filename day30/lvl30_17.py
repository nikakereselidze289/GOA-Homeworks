def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())

text = input("Enter the text: ")
word = input("Enter the word to count: ")

count = count_word_occurrences(text, word)
print(f"The word '{word}' appears {count} times.")
