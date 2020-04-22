import base64
from io import BytesIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import model.product as product
import model.wood as wood

def show_default_preview(model_id, wood_id):
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


def show_preview(model_id, wood_id, design_id, message):
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

    if message:
        draw = ImageDraw.Draw(result)
        font = ImageFont.truetype("static/fonts/Pacifico-Regular.ttf", 50, encoding='unic')
        w, h = draw.textsize(message, font=font)
        message_background = wood_type.crop((0, 0, w, h))
        result.paste(message_background, (int(((width - w) / 2)), int(((height - h) / 2))), message_background)
        draw.text(((width - w) / 2, (height - h) / 2), message, (110, 90, 60), font=font, align="right")

    img = BytesIO()
    result.save(img, format='PNG')
    img = img.getvalue()
    result_encoded = base64.b64encode(img)

    return result_encoded

