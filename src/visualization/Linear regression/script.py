import pandas as pd
import statsmodels.api as sm

X = df[attributes['features']].drop(attributes['target'], axis=1, errors="ignore")
if params['fit intercept']:
    X = sm.add_constant(X, prepend=False)

Y = df[attributes['target']]

mod = sm.OLS(Y, X)
res = mod.fit()

result = pd.concat([res.params, res.pvalues], axis=1).transpose()
result = pd.concat([pd.DataFrame({'': ['coefficient', 'p-value']}), result], axis=1)
result