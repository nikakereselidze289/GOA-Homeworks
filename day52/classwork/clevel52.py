# Get the mean of an array
def get_average(marks):
    raise NotImplementedError("TODO: get_average")
def get_average(marks):
    return int(sum(marks) / len(marks))


# Keep up the hoop
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"


# Reversed Words
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])



# Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s*27.777778)


# Switch it Up!
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]


# Function 2 - squaring an argument
def square(n):
    return n*n



# Removing Elements
def remove_every_other(my_list):
    return my_list[::2]

# 2nd variation
def remove_every_other(my_list):
    new_list = []
    
    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])
    
    return new_list


# Twice as old
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res


# All Star Code Challenge #18
def str_count(strng, letter):
    return strng.count(letter)

# Is it even?
def is_even(n): 
    return n % 2 == 0


# Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll*2



# Get Planet Name By ID
def get_planet_name(id):
    if id == 1: return "Mercury"
    elif id == 2: return "Venus"
    elif id == 3: return "Earth"
    elif id == 4: return "Mars"
    elif id == 5: return "Jupiter"
    elif id == 6: return "Saturn"
    elif id == 7: return "Uranus"
    elif id == 8: return "Neptune"
    
    
    
# Will there be enough space?
def enough(cap, on, wait):
    available = cap - on
    
    if available >= wait: return 0
    return wait - available



# What is between?
def between(a,b):
    return list(range(a, b+1))


# Is the string uppercase?
def is_uppercase(inp):
    return inp == inp.upper()


# Grasshopper - Debug sayHello
def say_hello(name):
    return "Hello, " + name



# Count the Monkeys!
def monkey_count(n):
    return list(range(1, n+1))



# Powers of 2
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]


# Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    
    cat_years = 24 + (human_years - 2) * 4
    dog_years = 24 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]