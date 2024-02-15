from typing import Dict

class HttpRequest:
  '''Structure for handling an HTTP request.

  Args:
    - header (Dict, optional): The request headers.
    - body (Dict, optional): The request body.
    - query_params (Dict, optional): The query parameters.

  Attributes:
    - header (Dict): The request headers.
    - body (Dict): The request body.
    - query_params (Dict): The query parameters.
  '''

  def __init__(self, header: Dict = None, body: Dict = None, query_params: Dict = None) -> None:
    '''Initializes the instance of the HttpRequest class.

    Args:
      - header (Dict, optional): The request headers.
      - body (Dict, optional): The request body.
      - query_params (Dict, optional): The query parameters.
    '''

    self.header = header
    self.body = body
    self.query_params = query_params
