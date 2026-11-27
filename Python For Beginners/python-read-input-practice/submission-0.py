def add_two_numbers() -> int:
    sum = 0
    insert = input()
    insert_holder = insert.split(",")
    for val in insert_holder:
        sum += int(val)
    
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
