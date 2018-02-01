"""test python OCR
"""

import io
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders

TOOL = pyocr.get_available_tools()[0]
LANG = TOOL.get_available_languages()[2]

req_image = []
final_text = []

IMAGE_PDF = Image(filename="./pdf/test.pdf")
image_jpeg = IMAGE_PDF.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    img_page.type = 'grayscale'
    with img[304:958, 410:476] as cropped:
        image = cropped.make_blob('jpeg')
        name = TOOL.image_to_string(
            PI.open(io.BytesIO(image)),
            lang=LANG,
            builder=pyocr.builders.TextBuilder()
        )
        print(name)
