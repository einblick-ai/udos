import pandas as pd

dummies = pd.get_dummies(df[[attributes['column'][0]]])
pd.concat([df, dummies], axis=1) if params['append'] else dummies