import os
from config import Config
from utils.pre_process import clean_log_data, create_log_embeddings
from models.rag_pipeline import RAGPipeline
from models.anomaly_detection import AnomalyDetectionModel
# from utils.reporting import generate_analysis_report

def run_analysis():
    # Load configuration
    config = Config()

    # Ingest and preprocess log data
    log_files = [os.path.join(config.LOG_DIR, f) for f in os.listdir(config.LOG_DIR)]
    print('Cleaning Logs')
    cleaned_logs = clean_log_data(log_files)
    print('Creating Embeddings of the input file')
    log_embeddings = create_log_embeddings(cleaned_logs)
    rgp = RAGPipeline(log_embeddings)
    print('Indexing with FAISS')
    rgp.index_with_faiss()
    # Define Query 
    query = "Can you summarize the log for me?"
    # Embedd Query
    print('Creating embedding for question')
    query_embeddings = create_log_embeddings(query)
    learned_context = rgp.similarity(query_embedding=query_embeddings, documents=cleaned_logs)

    output = rgp.generate_response(query, learned_context)
    print(output)

    # # Instantiate models
    # anomalies = anomaly_detector.detect_anomalies(log_embeddings)

    # # Generate report
    # generate_analysis_report(cleaned_logs, log_categories, anomalies, config.REPORT_OUTPUT_PATH)

if __name__ == "__main__":
    run_analysis()