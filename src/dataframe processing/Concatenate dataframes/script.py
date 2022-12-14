import numpy as np
import pandas as pd

ds0 = self.from_input(0).flatten()
ds1 = self.from_input(1).flatten()

for dfs in zip(ds0, ds1):
    first_columns = []
    second_columns = []

    if params["type"][0] == "horizontal":
        if dfs[0].shape[0] != dfs[1].shape[0]:
            raise ValueError("input dataframes must have the same number of rows")

        for c in dfs[0]:
            first_columns.append(c + params["first suffix"] if params["suffix all"] or c in dfs[1] else c)
            
        for c in dfs[1]:
            second_columns.append(c + params["second suffix"] if params["suffix all"] or c in dfs[0] else c)

        combined = pd.concat([dfs[0], dfs[1]], axis=1)
        combined.columns = np.concatenate((first_columns, second_columns))
        yield combined
    else:
        if dfs[0].shape[1] != dfs[1].shape[1]:
            raise ValueError("input dataframes must have the same number of columns")

        combined = pd.concat([dfs[0], dfs[1]], axis=0)
        combined.columns = dfs[0].columns
        yield combined