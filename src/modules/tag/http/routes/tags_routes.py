from flask import Blueprint, request

from src.modules.tag.http.controllers.tags_controller import TagsController
from src.shared.http.request import HttpRequest

tags_bp = Blueprint('tags', __name__)

@tags_bp.route('/tags', methods=['POST'])
def create():
  '''Endpoint for creating a new tag.

  Returns:
    - JSON: The response body.
  '''

  req = HttpRequest(body=request.json)

  tags_controller = TagsController()

  res = tags_controller.create(req)

  return res
