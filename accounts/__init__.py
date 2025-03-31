import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a stream handler (console logging only)
stream_handler = logging.StreamHandler()

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(stream_handler)