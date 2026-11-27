from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    return_list = []
    for age in age_dict.values():
        return_list.append(age)
        
    return return_list
# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
