import random
from datetime import datetime, timedelta
from loguru import logger

# Configure the log format
logger.add("sample_logs.txt", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

# Define log entry templates
log_templates = [
    "Application started",
    "User {user} logged in",
    "Disk space low on {host}",
    "Error processing request: {error}",
    "System {host} restarted"
]

# Generate 1000 log entries
for _ in range(1000):
    # Generate random log entry attributes
    user = f"user{random.randint(1, 100)}"
    host = f"host{random.randint(1, 50)}"
    error = f"Error code {random.randint(100, 999)}"
    log_level = random.choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    timestamp = datetime.now() - timedelta(seconds=random.randint(0, 3600 * 24 * 7))

    # Select a log template and format the log message
    log_template = random.choice(log_templates)
    log_message = log_template.format(user=user, host=host, error=error)

    # Log the message with the appropriate level
    logger.log(log_level, log_message)