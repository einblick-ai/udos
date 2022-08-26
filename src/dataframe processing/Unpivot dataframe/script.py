import pandas as pd

id_columns = attributes["ID columns"]
value_columns = attributes["Value columns"]


if len(value_columns) == 0:
    result = pd.melt(df, id_vars=id_columns)
else:
    result = pd.melt(df, id_vars=id_columns, value_vars=[c for c in value_columns if c not in id_columns])

result