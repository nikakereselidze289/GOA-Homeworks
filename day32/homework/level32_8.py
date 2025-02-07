def csv_to_list(csv_string):
    return csv_string.split(',')

csv_string = "apple,banana,orange,grape"
print(csv_to_list(csv_string))
