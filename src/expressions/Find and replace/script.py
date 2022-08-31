ds = self.from_input(0)

columnToSearch = params["find_replace"]["find_replace"]["find_in_column"]
newColumnName = params["find_replace"]["find_replace"]["new_column"]
c = ds.select(columnToSearch)

processedColumn = f"[{columnToSearch}]" if columnToSearch else ""
findReplacePairs = params["find_replace"]["find_replace"]["find_replace_pairs"]


validPairs = [p for p in findReplacePairs if len(p['find_keyword']) > 0]
replaceCalls = [f"replace({p['find_keyword']}, {p['replace_keyword']})" for p in validPairs]
findReplaceChain = ".".join(replaceCalls)

expression = f"[{columnToSearch}].{findReplaceChain}"

transformation = c.transformation(expression=expression, column=newColumnName)

for dfs in zip(ds.flatten(), transformation.flatten()):
    yield pd.concat([dfs[0], dfs[1]], axis=1)