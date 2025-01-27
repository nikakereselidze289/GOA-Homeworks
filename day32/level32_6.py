def insert_word_in_sentence(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return ' '.join(words)

sentence = "I am learning Python."
word = "really"
index = 2
print(insert_word_in_sentence(sentence, word, index))
