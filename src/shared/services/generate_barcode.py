from barcode import Code128
from barcode.writer import ImageWriter

class GenerateBarcodeService:
  '''A service class for generating barcodes using the Code128 format.

  Attributes:
    - base_path (str): The directory to save generated barcodes.
  '''

  base_path = 'public/barcodes/'

  def exec(self, product_code: str) -> str:
    '''Generates a barcode image for the given product code.

    Args:
      - product_code (str): The product code for which the barcode is generated.

    Returns:
      - str: The path where the generated barcode image is saved.
    '''

    barcode = Code128(product_code, ImageWriter("PNG", "RGB"))

    barcode_path = self.base_path + str(barcode)

    # Save in local storage
    barcode.save(barcode_path)

    return barcode_path
