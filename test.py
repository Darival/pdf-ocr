"""test python OCR
"""

import io
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders

TOOL = pyocr.get_available_tools()[0]
LANG = TOOL.get_available_languages()[2]

IMAGE_PDF = Image(filename="./pdf/test.pdf")
image_jpeg = IMAGE_PDF.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    img_page.type = 'grayscale'
    profile = {
        "name": [302, 968, 410, 476],
        "test_type": [394, 1492, 726, 790],
        "keys": [186, 566, 846, 1684],
        "values": [876, 1168, 846, 1684],
    }
    #img_page.save(filename='pikachu.jpg')
    
    for k, v in profile.items():
        with img_page[v[0]:v[1], v[2]:v[3]] as cropped:
            image = cropped.make_blob('jpeg')
            name = TOOL.image_to_string(
                PI.open(io.BytesIO(image)),
                lang=LANG,
                builder=pyocr.builders.TextBuilder()
            )
            # TODO this should be on a function
            text = list(filter(None, name.split('\n')))
            print(k, text, sep=' = ')
