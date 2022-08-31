import statsmodels.api as sm

fit = self.load_state(__state_id__)

dfs = []

for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)

X = df[attributes['Features']].drop(attributes['Target'], axis=1, errors="ignore")
if params['Fit intercept']:
    X = sm.add_constant(X, prepend=False)

yield pd.concat([pd.DataFrame({"prediction": fit.predict(exog=X)}), df], axis=1)