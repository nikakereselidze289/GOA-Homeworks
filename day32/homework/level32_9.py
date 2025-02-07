def paragraph_to_sentences(paragraph):
    return paragraph.split('.')

paragraph = "This is the first sentence. Here is the second one. And this is the third."
print(paragraph_to_sentences(paragraph))
