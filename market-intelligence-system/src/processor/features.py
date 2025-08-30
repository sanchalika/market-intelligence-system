from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

def compute_tfidf(texts):
return vectorizer.fit_transform(texts)