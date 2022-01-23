import sys

sys.path.append("../refactoring")
from computation import *

import pandas as pd
import pytest


@pytest.fixture
def df_fixture():
    df_ = pd.DataFrame([[1, 10], [5, 20]], columns=["num1", "num2"])
    yield df_


def test_compute_ratio(df_fixture):
    ratio = compute_ratio(df_fixture, numerator="num1", denominator="num2")
    assert ratio[0] == 0.1
    assert ratio[1] == 0.25
    assert len(ratio) == 2


def test_compute_correlations(df_fixture):
    correlations = compute_correlations(df_fixture)
    assert correlations == {"num1 and num2": 1.0}
