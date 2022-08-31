if params['min'] > params['max']:
    raise ValueError('min must cannot be more than max')
clamp = lambda value: params['max'] if value > params['max'] else params['min'] if value < params['min'] else value

ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        df[attributes['columns']] = df[attributes['columns']].apply(lambda column: column.apply(clamp))
        yield df
