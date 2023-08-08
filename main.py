import os
import json
import base64
import io
import numpy as np
from PIL import Image
import argparse

def read_name_file(name_path):
    with open(name_path, "r") as name_file:
        names = [name.strip() for name in name_file]
    return names

def convert_coor(size, xy):
    dw, dh = size
    x, y = xy
    return x / dw, y / dh

def convert(file, txt_name=None):
    if txt_name is None:
        txt_name = file.rstrip(".json") + ".txt"

    names = read_name_file('obj.names')
    with open(file, 'r') as f:
        Image.fromarray(img_b64_to_arr(json.loads(f.read())['imageData'])).save(txt_name.replace('txt', 'png'))
    
    with open(file, "r") as txt_file:
        js = json.loads(txt_file.read())

        with open(txt_name, "w") as txt_outfile:
            for item in js["shapes"]:
                label = item["label"]
                cls = [str(i) for i, name in enumerate(names) if label == name][0]

                height, width = js["imageHeight"], js["imageWidth"]

                for idx, pt in enumerate(item["points"]):
                    if idx == 0:
                        txt_outfile.write(cls)
                    x, y = pt
                    bb = convert_coor((width, height), [x, y])
                    txt_outfile.write(" " + " ".join([str(a) for a in bb]))

                txt_outfile.write("\n")

def img_data_to_pil(img_data):
    f = io.BytesIO()
    f.write(img_data)
    return Image.open(f)

def img_data_to_arr(img_data):
    return np.array(img_data_to_pil(img_data))

def img_b64_to_arr(img_b64):
    return img_data_to_arr(base64.b64decode(img_b64))

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to TXT")
    parser.add_argument('--input', type=str, help="Path to the input JSON file", required=True)
    parser.add_argument('--output', type=str, help="Path to the output TXT file", default=None)
    
    args = parser.parse_args()
    
    convert(args.input, args.output)

if __name__ == "__main__":
    main()
