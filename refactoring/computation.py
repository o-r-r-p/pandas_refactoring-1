import numpy as np
import itertools
from typing import List, Dict


def compute_ratio(df, numerator: str, denominator: str) -> List[float]:
    ratio = []
    for i, row in df.iterrows():
        try:
            ratio.append(float(row[numerator]) / float(row[denominator]))
        except:
            ratio.append(np.nan)
    return ratio


def compute_correlations(df) -> Dict[str, float]:
    correlations = {}
    for pair in itertools.combinations(df.columns, 2):
        corr = df[[pair[0], pair[1]]].corr().values[0, 1]
        correlations[f"{pair[0]} and {pair[1]}"] = corr
    return correlations
