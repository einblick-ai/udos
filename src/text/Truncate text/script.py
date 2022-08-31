ds = self.from_input(0)

truncate_length = int(params['truncate length'])        

for dfs in ds:
    for df in dfs:
        if truncate_length > 0:            
            for column in attributes['columns']:                
                df[column] = df[column].apply(lambda x: x[:truncate_length])
        yield df