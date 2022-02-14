split = df[attributes['column'][0]].str.split(params['delimiter'], expand=True, regex=params['use regex'], n=99)
split.columns = [attributes['column'][0] + '_' + str(i + 1) for i in range(split.shape[1])]
df[split.columns] = split