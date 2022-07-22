# examples of windows: ["30min", "1h", "2h", "3h", "6h", "1d", "2d"]

df = df.sort_values(by=[self._date] + self._group)
df[self._date] = pd.to_datetime(df[self._date], unit="ms")
df.index = df[self._date]

for window in self._windows:
    roll = df.groupby(by=self._group, sort=False).rolling(window, closed=self._closed)[self._columns].sum()
    roll = roll.sort_values(by=[self._date] + self._group)
    roll.columns += "_by_" +"_".join(self._group) + "_in_" + window
    df[roll.columns] = roll[roll.columns].values

return df.sample(frac=1)