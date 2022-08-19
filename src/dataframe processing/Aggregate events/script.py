import pandas as pd

# examples of windows: ["30min", "1h", "2h", "3h", "6h", "1d", "2d"]
windows = params["intervals"].split(";")
date = attributes['date'][0]
group = attributes['group']
closed = params['closed'][0]
columns = attributes['columns']

df = df.sort_values(by=[date] + group)
df[date] = pd.to_datetime(df[date], unit="ms")
df.index = df[date]

for window in windows:
    roll = df.groupby(by=group, sort=False).rolling(window, closed=closed)[columns].sum()
    roll = roll.sort_values(by=[date] + group)
    roll.columns += "_by_" +"_".join(group) + "_in_" + window
    df[roll.columns] = roll[roll.columns].values

df.sample(frac=1)