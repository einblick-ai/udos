for dfs in self.from_input(0):
    for df in dfs:
        for column in attributes['Columns']:
            df[column] = df[column].fillna(params['Fill value'])
        yield df