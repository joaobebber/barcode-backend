from typing import Dict

from src.shared.services.generate_barcode import GenerateBarcodeService

class CreateTagService:
  '''A service class for creating tags.'''

  def exec(self, product_code: str) -> Dict:
    '''Executes the creation of a tag for the given product code.

    Args:
      - product_code (str): The product code for which the tag is created.

    Returns:
      - Dict: A dictionary representing the created tag.
    '''

    generate_barcode = GenerateBarcodeService()

    tag_path = generate_barcode.exec(product_code)

    tag = {
      "type": "Tag Image",
      "count": 1,
      "path": f'{tag_path}.png'
    }

    return tag
