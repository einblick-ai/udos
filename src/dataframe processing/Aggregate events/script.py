import pandas as pd

# examples of windows: ["30min", "1h", "2h", "3h", "6h", "1d", "2d"]
windows = params["Intervals"].split(";")
date = attributes['Date'][0]
group = attributes['Group']
closed = params['Closed'][0]
columns = attributes['Columns']
aggregation_function = params['Aggregation function'][0]

df = df.sort_values(by=[date] + group)
df[date] = pd.to_datetime(df[date], unit="ms")
df.index = df[date]

for window in windows:
    groupby = df.groupby(by=group, sort=False).rolling(window, closed=closed)[columns]
    if aggregation_function == "Sum":
        roll = groupby.sum()
    elif aggregation_function == "Mean":
        roll = groupby.mean()
    elif aggregation_function == "Median":
        roll = groupby.median()
    elif aggregation_function == "Min":
        roll = groupby.min()
    elif aggregation_function == "Max":
        roll = groupby.max()
    roll = roll.sort_values(by=[date] + group)
    roll.columns += "_by_" +"_".join(group) + "_in_" + window
    df[roll.columns] = roll[roll.columns].values

df.sample(frac=1)