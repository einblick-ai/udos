if params['min'] > params['max']:
    raise ValueError('min must cannot be more than max')
clamp = lambda value: params['max'] if value > params['max'] else params['min'] if value < params['min'] else value
df[attributes['columns']] = df[attributes['columns']].apply(lambda column: column.apply(clamp))