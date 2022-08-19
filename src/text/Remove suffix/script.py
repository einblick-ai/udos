ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        for c in attributes['columns']:
            df[c] = df[c].apply(lambda s: s.removesuffix(params['suffix']))
        yield df