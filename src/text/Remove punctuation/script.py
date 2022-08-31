ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
        for column in attributes['columns']:            
            # https://stackoverflow.com/questions/50444346/fast-punctuation-removal-with-pandas            
            punct = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'   # `|` is not present here            
            transtab = str.maketrans(dict.fromkeys(punct, ''))
            df[column] = '|s|'.join(df[column].tolist()).translate(transtab).split('|s|')
        yield df