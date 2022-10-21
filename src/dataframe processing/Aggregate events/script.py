import pandas as pd

# examples of windows: ["30min", "1h", "2h", "3h", "6h", "1d", "2d"]
windows = params["intervals"].split(";")
date = attributes['date'][0]
group = attributes['group']
closed = params['closed'][0]
columns = attributes['columns']
aggregation_function = params['aggregation function'][0]

df = df.sort_values(by=[date] + group)
df[date] = pd.to_datetime(df[date], unit="ms")
df.index = df[date]

for window in windows:
    groupby = df.groupby(by=group, sort=False).rolling(window, closed=closed)[columns]
    if aggregation_function == "sum":
        roll = groupby.sum()
    elif aggregation_function == "mean":
        roll = groupby.mean()
    elif aggregation_function == "median":
        roll = groupby.median()
    elif aggregation_function == "min":
        roll = groupby.min()
    elif aggregation_function == "max":
        roll = groupby.max()
    roll = roll.sort_values(by=[date] + group)
    roll.columns += "_by_" +"_".join(group) + "_in_" + window
    df[roll.columns] = roll[roll.columns].values

df.sample(frac=1)