# common/logging.py
# Import the logging module for logging capabilities
# Import uuid to generate unique correlation IDs
import logging, uuid

# Function to get a logger with a specific name
def get_logger(name: str):
    # Create or retrieve a logger instance with the given name
    logger = logging.getLogger(name)
    
    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        # Create a stream handler to output logs to the console
        handler = logging.StreamHandler()
        
        # Define a custom log format that includes a correlation ID
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] [CID:%(cid)s] %(message)s")
        
        # Attach the formatter to the handler
        handler.setFormatter(formatter)

        handler.addFilter(CorrelationIdFilter())
        
        # Add the handler to the logger
        logger.addHandler(handler)
        
        # Set the logging level to INFO
        logger.setLevel(logging.INFO)

    
    return logger

# Custom logging filter to inject a correlation ID into each log record
class CorrelationIdContext:
    current_id = "N/A"

    @staticmethod
    def new_id() -> str:
        CorrelationIdContext.current_id = str(uuid.uuid4())
        return CorrelationIdContext.current_id

class CorrelationIdFilter(logging.Filter):
    def filter(self, record):
        record.cid = getattr(CorrelationIdContext, "current_id", "N/A")
        return True

