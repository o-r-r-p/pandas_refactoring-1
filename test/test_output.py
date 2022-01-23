import sys

sys.path.append("../refactoring")
from output import *


def test_print_dict():
    dict_ = {"You are": "Taro"}
    assert print_dict(dict_) == print("Monthly You are correlation is Taro")
