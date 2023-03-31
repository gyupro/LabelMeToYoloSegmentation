from glob import glob
import os
import json
from Convert import convert
import base64

import io
import PIL
from PIL import Image

import numpy as np
def img_data_to_pil(img_data):
    f = io.BytesIO()
    f.write(img_data)
    img_pil = PIL.Image.open(f)
    return img_pil


def img_data_to_arr(img_data):
    img_pil = img_data_to_pil(img_data)
    img_arr = np.array(img_pil)
    return img_arr

def img_b64_to_arr(img_b64):
    img_data = base64.b64decode(img_b64)
    img_arr = img_data_to_arr(img_data)
    return img_arr



for item in glob(r'label/*/*'):
    # print(item1)
    for item1 in glob(os.path.join(item, '*.json')):
        if os.path.isdir(item1):
            continue
        with open(item1, 'r') as f:
            Image.fromarray(img_b64_to_arr(json.loads(f.read())['imageData'])).save(item1.replace('json', 'png'))
    convert(item)

