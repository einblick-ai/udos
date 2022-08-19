ds = self.from_input(0)

for dfs in ds:
    returned = False
    for df in dfs:
        if not returned:
            returned = True
            yield df.head(params['number of rows'])