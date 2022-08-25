import pandas as pd
import statsmodels.api as sm

dfs = []

for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)
print(df)

X = df[attributes['features']].drop(attributes['target'], axis=1, errors="ignore")
if params['fit intercept']:
    X = sm.add_constant(X, prepend=False)

Y = df[attributes['target']]

model = sm.OLS(Y, X)
fit = model.fit()

self.save_state(fit)

result = pd.concat([fit.params, fit.pvalues], axis=1).transpose()
result = pd.concat([pd.DataFrame({'': ['coefficient', 'p-value']}), result], axis=1)
yield result