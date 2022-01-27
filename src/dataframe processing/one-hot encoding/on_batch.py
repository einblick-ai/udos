dummies = pd.get_dummies(df[[attributes['column'][0]]])

return pd.concat([df, dummies], axis=1) if params['append columns'] else dummies