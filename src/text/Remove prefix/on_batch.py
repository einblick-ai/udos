for c in attributes['columns']:
    df[c] = df[c].apply(lambda s: s.removeprefix(params['prefix']))
return df