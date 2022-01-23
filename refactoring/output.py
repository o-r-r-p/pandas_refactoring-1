from typing import Dict


def print_dict(dict: Dict[str, float]):
    for key in dict.keys():
        value = dict[key]
        print("Monthly {} correlation is {}".format(key, value))
