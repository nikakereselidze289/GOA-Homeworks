sentence = input("Enter a sentence: ")
position = sentence.find("Python")

if position != -1:
    print(f"The word 'Python' is found at position: {position}")
else:
    print("The word 'Python' was not found.")