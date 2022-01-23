import pandas as pd
import numpy as np
import datetime as dt
from typing import List, Union


def read_csv(path: str):
    return pd.read_csv(path)


def particular_data_point(df, data_point: str, column_for_the_point: str):
    return df[df[column_for_the_point] == data_point]


def inner_join(df1, df2):
    return pd.merge(df1, df2, how="inner")


def outliers_to_nan(df, column_list: List[str], threshold: Union[int, float]):
    for column in column_list:
        df.loc[df[column] < threshold, column] = np.nan
    return df


def to_datetype(df, column: Union[int, str]):
    df[column] = pd.to_datetime(df[column].astype("str"))
    return df


def add_month_column(df, date_column: str):
    df["MONTH"] = df[date_column].dt.month
    return df


def groupby_sum(df, groupby: str, extracted_columns: List[str]):
    return df.groupby([groupby])[extracted_columns].agg(sum)


def groupby_mean(df, groupby: str, extracted_columns: List[str]):
    return df.groupby([groupby])[extracted_columns].agg(np.mean)
