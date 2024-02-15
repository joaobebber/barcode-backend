from src.modules.tag.services.create_tag import CreateTagService
from src.shared.http.request import HttpRequest
from src.shared.http.response import HttpResponse

class TagsController:
  '''Controller for handling tag-related HTTP requests.'''

  def create(self, http_request: HttpRequest):
    '''Handles the creation of a new tag.

    Args:
      - http_request (HttpRequest): The HTTP request object containing the request body.

    Returns:
      - HttpResponse: The HTTP response object containing the response body.
    '''

    body = http_request.body
    product_code = body["product_code"]

    create_tag = CreateTagService()

    tag = create_tag.exec(product_code)

    return HttpResponse(status_code=201, body={ "tag": tag }).send()
