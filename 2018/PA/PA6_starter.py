from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

class SentimentAnalyzer:

    def __init__(self):
        self.model = LogisticRegression()
        self.dict_vectorizer = DictVectorizer()
        self.train(self.model)

    def train(self, model: LogisticRegression):
        """Train sentiment analyzer

        Open the yelp review dataset and train the model
        """
        pass
        

    def classify_sentiment(self, text: str):
        """Classify the sentiment of the text

        Return:
            one of "positive", "neutral", "negative"

        >>> analyzer.classify_sentiment('I absolutely hate this place.')
        'negative'
        """
        return 'neutral' # replace this line with a clever answer

    def get_top_features(self, label: str, top_k: int):
        """Get top k features for the given label

        >>> analyzer.get_top_features('positive', 2)
        ['great', 'excellent']
        """
        pass
