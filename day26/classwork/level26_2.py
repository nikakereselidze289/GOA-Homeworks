def manual_range(start, end, step):
    for num in range(start, end, step):
        if num % 2 == 0:
            print(num)

manual_range(0, 20, 2)
manual_range(1, 10, 3)
manual_range(10, 50, 5)
manual_range(0, 30, 4)
manual_range(5, 25, 3)
