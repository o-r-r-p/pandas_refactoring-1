import sys

sys.path.append("../refactoring")
from preprocessing import *

import pandas as pd
import pytest


@pytest.fixture
def fixture1():
    df_ = pd.DataFrame(
        [["abcd", -10, 3], ["abcd", -4, -2], ["efgh", 5, 1]],
        columns=["letters", "num1", "num2"],
    )
    yield df_


@pytest.fixture
def fixture2():
    df_ = pd.DataFrame(
        [
            ["abcd", "20201209", "20150405"],
            ["efgh", "20191110", "20121231"],
            ["ijkl", "20191012", "20151130"],
        ],
        columns=["letters", "str_date", "date"],
    )
    df_["date"] = pd.to_datetime(df_["date"])
    yield df_


def test_read_csv():
    path = "test_data/test.csv"
    df_ = read_csv(path=path)
    assert df_.shape == (3, 3)


def test_particular_data_point(fixture1):
    df_ = particular_data_point(
        df=fixture1, data_point="abcd", column_for_the_point="letters"
    )
    assert len(df_["letters"].unique()) == 1
    assert len(df_) == 2
    assert df_.shape == (2, 3)


def test_inner_join(fixture1, fixture2):
    df_ = inner_join(df1=fixture1, df2=fixture2)
    assert df_.shape == (3, 5)


def test_outliers_to_nan(fixture1):
    df_ = outliers_to_nan(df=fixture1, column_list=["num1", "num2"], threshold=1)
    assert df_["num1"].isnull().sum() == 2
    assert df_["num2"].isnull().sum() == 1


def test_to_datetype(fixture2):
    df_ = to_datetype(df=fixture2, column="str_date")
    assert df_["str_date"][0] == pd.to_datetime("20201209")
    assert df_["str_date"][1] == pd.to_datetime("20191110")
    assert df_["str_date"][2] == pd.to_datetime("20191012")

# yahh
def test_add_month_column(fixture2):
    df_ = add_month_column(df=fixture2, date_column="date")
    assert df_.shape == (3, 4)
    assert df_["MONTH"][0] == 4
    assert df_["MONTH"][1] == 12
    assert df_["MONTH"][2] == 11


def test_groupby_sum(fixture1):
    df_ = groupby_sum(
        df=fixture1, groupby="letters", extracted_columns=["num1", "num2"]
    )
    assert df_.shape == (2, 2)
    assert df_["num1"][0] == -14
    assert df_["num2"][1] == 1


def test_groupby_mean(fixture1):
    df_ = groupby_mean(
        df=fixture1, groupby="letters", extracted_columns=["num1", "num2"]
    )
    assert df_.shape == (2, 2)
    assert df_["num1"][0] == -7
    assert df_["num2"][1] == 1
