import pandas as pd

dfs = []

for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)

vectorizer = self.load_state(__state_id__)

s = df[attributes["target"][0]].tolist()
vector = vectorizer.transform(s).todense()
vector_df = pd.DataFrame(vector, columns = vectorizer.get_feature_names())

df[vectorizer.get_feature_names()] = vector_df.values

yield df