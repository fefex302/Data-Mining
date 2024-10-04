import pandas as pd

def merge_dataset(dataset1: pd.DataFrame, dataset2: pd.DataFrame, key_left: str, key_right: str):

    return pd.merge(dataset1, dataset2, left_on=key_left, right_on=key_right)