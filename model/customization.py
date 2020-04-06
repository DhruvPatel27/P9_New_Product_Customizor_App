import base64
from io import BytesIO

from PIL import Image

import model.product as product
import model.wood as wood


def wood_preview(model_id, wood_id):
    mask = product.get_products_mask(model_id)
    mask = Image.open(BytesIO(base64.b64decode(mask[0]['model_mask'].decode('utf-8'))))
    mask = mask.convert("RGBA")
    width, height = mask.size

    wood_type = wood.get_wood_by_id(wood_id)
    wood_type = Image.open(BytesIO(base64.b64decode(wood_type['image'].decode('utf-8'))))
    wood_type = wood_type.convert("RGBA")
    files = [wood_type, mask]

    result = Image.new("RGBA", (width, height))

    for i in range(0, len(files)):
        result.paste(files[i], (0, 0), files[i])

    img = BytesIO()
    result.save(img, format='PNG')
    img = img.getvalue()
    result_encoded = base64.b64encode(img)
    return result_encoded


def design_preview(model_id, wood_id, design_id):
    mask = product.get_products_mask(model_id)
    mask = Image.open(BytesIO(base64.b64decode(mask[0]['model_mask'].decode('utf-8'))))
    mask = mask.convert("RGBA")
    width, height = mask.size

    wood_type = wood.get_wood_by_id(wood_id)
    wood_type = Image.open(BytesIO(base64.b64decode(wood_type['image'].decode('utf-8'))))
    wood_type = wood_type.convert("RGBA")

    design_type = wood.get_design_by_id(design_id)
    design_type = Image.open(BytesIO(base64.b64decode(design_type['mask'].decode('utf-8'))))
    design_type = design_type.convert("RGBA")

    files = [wood_type, design_type, mask]

    result = Image.new("RGBA", (width, height))

    for i in range(0, len(files)):
        result.paste(files[i], (0, 0), files[i])

    img = BytesIO()
    result.save(img, format='PNG')
    img = img.getvalue()
    result_encoded = base64.b64encode(img)
    return result_encoded
