from typing import Dict
from flask import Response, jsonify

class HttpResponse:
  '''Structure for handling an HTTP response.

  Args:
    - status_code (int): The status code of the response.
    - body (Dict): The response body.

  Attributes:
    - status_code (int): The status code of the response.
    - body (Dict): The response body.
  '''

  def __init__(self, status_code: int, body: Dict) -> None:
    '''Initializes the instance of the HttpResponse class.

    Args:
      - status_code (int): The status code of the response.
      - body (Dict): The response body.
    '''

    self.status_code = status_code
    self.body = body

  def send(self) -> tuple[Response, int]:
    '''Sends the formatted HTTP response.

    Returns:
      - tuple[Response, int]: A tuple containing the response and status code.
    '''

    return jsonify(self.body), self.status_code
