# Endpoints

## /tags

- [POST] /tags
  * _Request_: {
    "product_code": "123-456-789"
  }
  * _Response_: {
    "tag": {
      "count": 1,
      "path": "public/barcodes/123-456-789.png",
      "type": "Tag Image"
    }
  }
