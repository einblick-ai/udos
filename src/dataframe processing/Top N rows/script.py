top = None
ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        batch_result = df.nlargest(
            int(params["number of rows"]), attributes["column"][0])
        top = pd.concat([top, batch_result], axis=0).nlargest(int(
            params["number of rows"]), attributes["column"][0]) if top is not None else batch_result
        yield top
