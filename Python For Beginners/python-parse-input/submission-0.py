from typing import List

def read_integers() -> List[int]:
    user_input = input()
    holder_list = user_input.split(",")
    return_list = []
    for hold in holder_list:
        return_list.append(int(hold))
    return return_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
