import string 

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords  
from nltk.tokenize import wordpunct_tokenize

if params['stem words'] or params['remove stop words']:
    self._tokenizer = wordpunct_tokenize
    if params['stem words']:
        self._stemmer = PorterStemmer()
    if params['remove stop words']:
        # from: nltk.download('stopwords'), english component
        self._stopwords = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])


ds = self.from_input(0)

for dfs in ds:
    for df in dfs:
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
        
        yield df