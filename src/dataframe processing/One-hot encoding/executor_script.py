import pandas as pd

encoder = self.load_state(__state_id__)

dfs = []

for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)

result = pd.DataFrame(encoder.transform(df[attributes['Columns']]), columns=encoder.get_feature_names(attributes['Columns']))
if not params['Keep original columns']:
    df = df.drop(attributes['Columns'], axis=1)
yield pd.concat([df.reset_index(drop=True), result], axis=1)