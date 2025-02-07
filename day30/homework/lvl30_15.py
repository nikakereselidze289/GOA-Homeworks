paragraph = input("Enter a paragraph: ")
count = paragraph.lower().split().count("the")
print(f"The word 'the' appears {count} times.")
