splits = [df[column].str.split(params['delimiter'], expand=True, regex=params['use regex'], n=99) for column in attributes['columns']]
for i, split in enumerate(splits):
    split.columns = [attributes['columns'][i] + '_' + str(j + 1) for j in range(split.shape[1])]
    df[split.columns] = split
df