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
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] [CID:%(correlation_id)s] %(message)s'
        )
        
        # Attach the formatter to the handler
        handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(handler)
        
        # Set the logging level to INFO
        logger.setLevel(logging.INFO)

    # Add the filter here to inject correlation_id into all log records
    logger.addFilter(CorrelationIdFilter())
    
    return logger

# Custom logging filter to inject a correlation ID into each log record
class CorrelationIdFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        # Generate a unique correlation ID using UUID
        self.correlation_id = uuid.uuid4()
    
    # This method is called for each log record
    def filter(self, record):
        # Add the correlation ID to the log record
        record.correlation_id = self.correlation_id
        return True


#logger = get_logger("my_app")
#logger.addFilter(CorrelationIdFilter())
#logger.info("This is a test log message.")
