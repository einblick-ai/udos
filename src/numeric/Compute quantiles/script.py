ds = self.from_input(0)

output_column_name = attributes['column'][0] + \
    "_quantile" if params['output column name'] == "" else params['output column name']

for dfs in ds:
    for df in dfs:
        df[output_column_name] = pd.qcut(df[attributes['column'][0]],
                                         params['number of quantiles'], duplicates='drop', labels=False)
        yield df
