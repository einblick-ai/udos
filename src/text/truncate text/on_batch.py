truncate_length = int(params['truncate length'])        
if truncate_length > 0:            
    for column in attributes['columns']:                
        df[column] = df[column].apply(lambda x: x[:truncate_length])
return df