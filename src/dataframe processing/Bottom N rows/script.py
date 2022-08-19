bottom = None
ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        batch_result = df.nsmallest(
            int(params["number of rows"]), attributes["column"][0])
        bottom = pd.concat([bottom, batch_result], axis=0).smallest(int(
            params["number of rows"]), attributes["column"][0]) if bottom is not None else batch_result
        yield bottom
