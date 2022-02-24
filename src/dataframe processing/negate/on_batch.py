for column in attributes['columns']:
        df[column if params['in place'] else column + '_negated'] = df[column].apply(lambda x: not x)