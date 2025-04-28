reverse_and_capitalize = lambda s: s[::-1].capitalize()

print(reverse_and_capitalize("hello"))      
print(reverse_and_capitalize("python"))     
print(reverse_and_capitalize("school"))     

# ანონიმური ფუნქცია, რომელიც რიცხვს ორმაგებს და ეგრევე გამოიძახება
print((lambda x: x * 2)(10))
