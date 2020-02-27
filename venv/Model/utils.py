import base64

# Encode image into base64 string
def image_encoding(img_file):
    base64_string = base64.b64encode(img_file.read())
    return base64_string


# Decode base64 string to image
def image_decoding(base64_string):
    img_data = base64.b64decode(base64_string)
    return img_data

