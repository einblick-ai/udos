for c in attributes['columns']:
    df[c] = df[c].apply(lambda s: s.removesuffix(params['suffix']))
return df