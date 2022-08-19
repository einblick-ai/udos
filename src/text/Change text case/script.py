ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        for column in attributes['columns']:
            if params['casing'][0] == "lowercase":
                df[column] = df[column].str.lower()
            elif params['casing'][0] == "uppercase":
                df[column] = df[column].str.upper()
            elif params['casing'][0] == "capitalize":
                df[column] = df[column].str.title()
        yield df
