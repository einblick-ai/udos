import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords  
from nltk.tokenize import wordpunct_tokenize
from copy import deepcopy
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


dfs = []

for df in self.from_input(0).flatten():
    dfs.append(df)

df = pd.concat(dfs, axis=0)

args = {
    "max_df": 0.95,
    "min_df": 2,
    "max_features": params["Max words"],
    "stop_words": "english",
    "ngram_range": (1, params["Max ngram"])
}

vectorizer = TfidfVectorizer(**args) if params["Extractor type"] == "TF/IDF" else CountVectorizer(**args)

s = df[attributes["Target"][0]].tolist()
vectorizer.fit(s)

self.save_state(vectorizer)