# Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))


# Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    
    if rules[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    
        # Is n divisible by x and y?
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


# If you can't sleep, just count sheep!!
def count_sheep(n):
    return ''.join([f"{i} sheep..." for i in range(1, n + 1)]).strip()


# Grasshopper - Grade book
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'