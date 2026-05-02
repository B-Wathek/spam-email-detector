from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def build_model():
    vectorizer = TfidfVectorizer(stop_words='english')
    model = LogisticRegression()
    return vectorizer, model
