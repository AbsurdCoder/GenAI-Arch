import numpy as np
from sklearn.covariance import EllipticEnvelope
from utils.pre_process import create_log_embeddings

class AnomalyDetectionModel:
    def __init__(self, contamination=0.01):
        self.contamination = contamination
        self.model = EllipticEnvelope(contamination=self.contamination)

    def fit(self, log_embeddings):
        """
        Train the anomaly detection model using the provided log embeddings.
        
        Args:
            log_embeddings (List[List[float]]): List of log entry embeddings.
        """
        self.model.fit(log_embeddings)

    def detect_anomalies(self, log_embeddings):
        """
        Detect anomalies in the given log embeddings.
        
        Args:
            log_embeddings (List[List[float]]): List of log entry embeddings.
        
        Returns:
            List[bool]: List of boolean values indicating if each log entry is an anomaly or not.
        """
        anomaly_scores = self.model.decision_function(log_embeddings)
        return anomaly_scores < 0