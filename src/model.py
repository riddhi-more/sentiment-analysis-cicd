"""
Machine Learning model for sentiment analysis
Uses scikit-learn for classification
"""

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

class SentimentModel:
    """
    Sentiment analysis model using Logistic Regression
    """
    
    def __init__(self):
        """Initialize the model and vectorizer"""
        self.model = LogisticRegression(max_iter=1000)
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.is_trained = False
    
    def train(self, texts, labels):
        """
        Train the model
        
        Args:
            texts: List of text samples
            labels: List of labels (positive, negative, neutral)
        """
        # Convert texts to numbers
        X = self.vectorizer.fit_transform(texts)
        
        # Train model
        self.model.fit(X, labels)
        self.is_trained = True
    
    def predict(self, text):
        """
        Predict sentiment of text
        
        Args:
            text: Input text to classify
        
        Returns:
            Predicted sentiment label
        """
        if not self.is_trained:
            raise ValueError("Model not trained yet")
        
        X = self.vectorizer.transform([text])
        prediction = self.model.predict(X)
        return prediction[0]
    
    def save(self, filepath):
        """Save model to disk"""
        joblib.dump(self.model, filepath)
        joblib.dump(self.vectorizer, filepath + ".vec")
    
    def load(self, filepath):
        """Load model from disk"""
        self.model = joblib.load(filepath)
        self.vectorizer = joblib.load(filepath + ".vec")
        self.is_trained = True
