def manual_find(main_string, str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i+len(str_to_find)] == str_to_find:
            return i
    return -1

main_string = "hello world"
str_to_find = "world"
print(manual_find(main_string, str_to_find))  
