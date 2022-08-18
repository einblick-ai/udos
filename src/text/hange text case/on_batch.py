for column in attributes['columns']:         
    if params['casing'][0] == "lowercase":                
        df[column] = df[column].str.lower()         
    elif params['casing'][0] == "uppercase":                
        df[column] = df[column].str.upper()          
    elif params['casing'][0] == "capitalize":                                
        df[column] = df[column].str.title()        
return df