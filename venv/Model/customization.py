import base64
from io import BytesIO

from PIL import Image


def mask_loop(mask, wood):
    mask = Image.open(BytesIO(base64.b64decode(mask)))
    mask = mask.convert("RGBA")
    wood = Image.open(BytesIO(base64.b64decode(wood)))
    wood = wood.convert("RGBA")
    files = [wood, mask]

    result = Image.new("RGBA", (1000, 1000))

    for i in range(0, len(files)):
        result.paste(files[i], (0, 0), files[i])
    return result
