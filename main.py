from PIL import Image

from pillow_heif import register_heif_opener

import pytesseract


register_heif_opener()

img = Image.open('./data/images/farm-boy.HEIC')
img = img.convert("RGB")

print(pytesseract.image_to_string(img))