from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from utils.pre_process import create_log_embeddings

class TextClassificationModel:
    def __init__(self, num_classes):
        self.num_classes = num_classes
        self.model = OneVsRestClassifier(LogisticRegression())

    def fit(self, log_embeddings, log_labels):
        """
        Train the text classification model using the provided log embeddings and labels.
        
        Args:
            log_embeddings (List[List[float]]): List of log entry embeddings.
            log_labels (List[int]): List of integer labels for each log entry.
        """
        self.model.fit(log_embeddings, log_labels)

    def predict(self, log_embeddings):
        """
        Predict the classes of the given log embeddings.
        
        Args:
            log_embeddings (List[List[float]]): List of log entry embeddings.
        
        Returns:
            List[int]: List of predicted class labels for each log entry.
        """
        return self.model.predict(log_embeddings)