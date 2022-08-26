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

stop_words = set()

if params['stem words'] or params['remove stop words']:
    # tokenizer = wordpunct_tokenize
    # if params['stem words']:
    #     stemmer = PorterStemmer()
    if params['remove stop words']:
        # from: nltk.download('stopwords'), english component
        stop_words = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])

args = {
    "max_df": 0.95,
    "min_df": 2,
    "max_features": params["max words"],
    "stop_words": "english",
    "ngram_range": (1, params["max ngram"])
}

vectorizer = TfidfVectorizer(**args) if params["extractor type"] == "TF/IDF" else CountVectorizer(**args)

s = df[attributes["target"][0]].tolist()
vectorizer.fit(s)

# vectorizer = WordExtractor( max_df=0.95,
#                             min_df=2,
#                             max_features=params["max words"],
#                             stop_words='english',
#                             ngram_range=(1, params["max ngram"]),
#                             target=attributes["target"][0],
#                             extractor_type=params["extractor type"])
# vectorizer.fit(df) 

self.save_state(vectorizer)