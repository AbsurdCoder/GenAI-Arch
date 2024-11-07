# log_analysis/utils/data_processing.py

import os
import re
import pickle
from typing import List
import json
from config import Config

def data_loader(log_files: List[str]) -> List[str]:
    """
    Load the log file
    Args: log_files (List[str]): List of file paths to log files.
    Returns: List[str]: List of logs
    """
    data = [json.loads(line) for line in open(log_files, 'r')]
    return data

def clean_log_data(log_files: List[str]) -> List[str]:
    """
    Clean and preprocess log data from the given list of log file paths. 
    Args: log_files (List[str]): List of file paths to log files.
    Returns: List[str]: List of cleaned and preprocessed log entries.
    """
    cleaned_logs = []
    for log_file in log_files:
        with open(log_file, 'r') as f:
            for line in f:
                # Remove any ANSI escape codes for color formatting
                line = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', line)
                # Remove any leading/trailing whitespace
                line = line.strip()
                # Add the cleaned line to the list
                cleaned_logs.append(line)
    return cleaned_logs

def create_log_embeddings(log_entries: List[str]) -> List[List[float]]:
    """
    Create embeddings for the given list of log entries using the OpenAI API.
    Args: log_entries (List[str]): List of log entries to be embedded.
    Returns: List[List[float]]: List of embeddings, where each embedding is a list of float values.
    """
    from utils.model_helpers import ollama_helpers
    
    oh = ollama_helpers()
    embeddings = []
    for entry in log_entries:
        embedding = oh.embedding(text=entry)
        embeddings.append(embedding)
    return embeddings

def save_embeddings(embeddings, output_path):
    """
    Save a list of embeddings to a file.
    Args: embeddings (List[List[float]]): List of embeddings to be saved.
    output_path (str): Path to the output file.
    """
    with open(output_path, 'wb') as f:
        pickle.dump(embeddings, f)

def load_embeddings(input_path):
    """
    Load a list of embeddings from a file.
    Args: input_path (str): Path to the input file.
    Returns: List[List[float]]: List of loaded embeddings.
    """
    with open(input_path, 'rb') as f:
        return pickle.dump(f)