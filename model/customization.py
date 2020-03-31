import base64
from io import BytesIO

from PIL import Image

def mask_loop(mask, wood_type, design_type):
    mask = Image.open(BytesIO(base64.b64decode(mask.decode('utf-8'))))
    mask = mask.convert("RGBA")
    width, height = mask.size
    wood = Image.open(BytesIO(base64.b64decode(wood_type.decode('utf-8'))))
    wood = wood.convert("RGBA")
    design = Image.open(BytesIO(base64.b64decode(design_type.decode('utf-8'))))
    design = design.convert("RGBA")
    files = [wood, design, mask]

    result = Image.new("RGBA", (width, height))

    for i in range(0, len(files)):
        result.paste(files[i], (0, 0), files[i])

    img = BytesIO()
    result.save(img, format='PNG')
    img = img.getvalue()
    result_encoded = base64.b64encode(img)
    return result_encoded



