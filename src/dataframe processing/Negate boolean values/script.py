ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        for column in attributes['columns']:
            df[column if params['in place'] else column + '_negated'] = df[column].apply(lambda x: not x)        
        yield df