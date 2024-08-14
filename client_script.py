import requests
import json
import logging

# Configure logging
logging.basicConfig(
    filename='api_call.log',  # You can adjust the log file name here
    filemode='a',
    format='[%(asctime)s] [%(levelname)s] [%(filename)s] [%(lineno)s:%(funcName)s()] %(message)s',
    datefmt='%Y-%b-%d %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)

log_level_env = 'INFO'  # You can adjust the log level here
log_level_dict = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}
if log_level_env in log_level_dict:
    log_level = log_level_dict[log_level_env]
else:
    log_level = log_level_dict['INFO']
LOGGER.setLevel(log_level)

def api_calls(url,Question,port):

    """
    Make an API call to the specified URL and port, passing the given question as a query parameter.

    Parameters:
    - url (str): The base URL of the server.
    - question (str): The question to be sent as a query parameter.
    - port (int): The port on which the server is running.

    Returns:
    - dict or str: The JSON response from the server if successful, or an error message with the status code.
    """
    try:

      LOGGER.info("Your Response Generating...")
      # Make a GET request to the server with the question as a query parameter
      response = requests.get(f"{url}:{port}?question={Question}")

      # Check if the request was successful (status code 200)
      if response.status_code == 200:
          # Return the JSON response
          return response.json()
      else:
          # Return an error message with the status code
          return "Error:", response.status_code
    except Exception as e:
            return str(e)
  
url = 'http://localhost'  # Replace with your server address if needed
Question = 'Hello, server!'
port = 8000
result = api_calls(url,Question,port)
print(result)