new_col = pd.qcut(df[attributes['column'][0]], params['# quantiles'], labels=False)
df[attributes['column'][0] + "_quantile"] = [x + 1 for x in new_col]