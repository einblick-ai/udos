previous = [pair["Key"] for pair in params['columns to rename']]
new = [pair["Value"] for pair in params['columns to rename']]

d = dict(zip(previous, new))

yield df.rename(d, axis=1)