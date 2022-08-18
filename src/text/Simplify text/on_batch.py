import string 


truncate_length = int(params['truncate length'])

for column in attributes['columns']:
    if params['casing'][0] == "lowercase":
        df[column] = df[column].str.lower()
    elif params['casing'][0] == "uppercase": 
        df[column] = df[column].str.upper()

    if params['remove stop words']:
        df[column] = df[column].apply(lambda sentence: ' '.join([w for w in self._tokenizer(sentence) if (w not in string.punctuation and w not in self._stopwords)]))
    
    if params['stem words']:
        df[column] = df[column].apply(lambda sentence: ' '.join([self._stemmer.stem(w) for w in self._tokenizer(sentence)]))

    if params['remove punctuation']:
        # https://stackoverflow.com/questions/50444346/fast-punctuation-removal-with-pandas
        punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'   # `|` is not present here
        transtab = str.maketrans(dict.fromkeys(punct, ''))
        df[column] = '|s|'.join(df[column].tolist()).translate(transtab).split('|s|')   

    if params['sort alphabetically']:
        df[column] = [' '.join(sorted(e)) for e in df[column].str.split()]

    if params['normalize']:
        df[column] = df[column].str.normalize("NFC")

    if truncate_length > 0:
        df[column] = df[column].apply(lambda x: x[:truncate_length])