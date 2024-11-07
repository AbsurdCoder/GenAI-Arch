import os
from config import Config
from utils.data_processing import clean_log_data, create_log_embeddings
from models.text_classification import TextClassificationModel
from models.anomaly_detection import AnomalyDetectionModel
from utils.reporting import generate_analysis_report

def run_analysis():
    # Load configuration
    config = Config()

    # Ingest and preprocess log data
    log_files = [os.path.join(config.LOG_DIR, f) for f in os.listdir(config.LOG_DIR)]
    cleaned_logs = clean_log_data(log_files)
    log_embeddings = create_log_embeddings(cleaned_logs)

    # Instantiate models
    text_classifier = TextClassificationModel()
    anomaly_detector = AnomalyDetectionModel()

    # Make predictions
    log_categories = text_classifier.predict(log_embeddings)
    anomalies = anomaly_detector.detect_anomalies(log_embeddings)

    # Generate report
    generate_analysis_report(cleaned_logs, log_categories, anomalies, config.REPORT_OUTPUT_PATH)

if __name__ == "__main__":
    run_analysis()