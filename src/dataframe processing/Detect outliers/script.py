from sklearn.ensemble import IsolationForest

columns = attributes['columns']
df = df.dropna()

if params['strictness'] != 0:
    strictness = 1/(params['strictness']+2)
    outlier_column = IsolationForest(contamination=strictness, random_state=0).fit_predict(df[columns].values)
else:
    outlier_column = IsolationForest(random_state=0).fit_predict(df[columns].values) # auto

df.insert(0, "outlier", outlier_column.replace(to_replace={-1: "yes", 1: "no"}))

df