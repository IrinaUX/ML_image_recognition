import re
from PIL import Image
from io import BytesIO
import base64
import numpy as np


def b64_PIL(b64img):
    data = re.sub('^data:image/.+;base64,', '', b64img)
    img_PIL = Image.open(BytesIO(base64.b64decode(data)))
    return img_PIL


def num_b64(img_data):
    image = Image.fromarray(img_data.astype('uint8'), 'RGB')
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return u"data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")

