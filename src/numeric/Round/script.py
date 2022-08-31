f = lambda x: x.apply(lambda y: round(y, params['decimal places']) if y >= 0 else int(round(y, params['decimal places'])))

ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        df[attributes['columns']] = df[attributes['columns']].apply(f)
        yield df