student_info = {
    'name': 'ნიკა',
    'surname': 'კერესელიძე',
    'academy': 'GOA',
    'fav-color': 'ლურჯი',
    'city': 'თბილისი',
    'goa-student': True,
    'age': 15,
    'fav-programming-lang': 'Python'
}

for key, value in student_info.items():
    print(f"{key}: {value}")



# 2nd classwork
my_dict = {
    'name': 'nika',
    'age': 15,
    'city': 'Tbilisi',
    'occupation': 'developer',
    'hobby': 'play basketball'
}

print("Keys:", my_dict.keys())

print("Values:", my_dict.values())

print("Items:", my_dict.items())

for key, value in my_dict.items():
    print(f"{key}: {value}")
