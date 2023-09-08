import os
import json
import base64
import numpy as np
from PIL import Image

def read_name_file(name_path):
    with open(name_path, "r") as name_file:
        names = [name.strip() for name in name_file]
    return names

def img_to_b64(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def convert_yolo_to_labelme(yolo_file, image_path, json_name=None):
    if json_name is None:
        json_name = yolo_file.rstrip(".txt") + ".json"
    
    names = read_name_file('obj.names')
    img = Image.open(image_path)
    width, height = img.size

    data = {
        "version": "5.3.1",
        "flags": {},
        "shapes": [],
        "imagePath": os.path.basename(image_path),
        "imageData": img_to_b64(image_path),
        "imageHeight": height,
        "imageWidth": width,
    }

    with open(yolo_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            cls = int(parts[0])
            pts = [float(x) for x in parts[1:]]
            
            
            
            shape = {
                "label": names[cls],
                "line_color": None,
                "fill_color": None,
                "points": [[pts[i] * width, pts[i + 1] * height] for i in range(0, len(pts), 2)],  # rectangle represented as a polygon
                "shape_type": "polygon",
                "flags": {}
            }

            data["shapes"].append(shape)
    
    with open(json_name, "w") as json_outfile:
        json.dump(data, json_outfile, ensure_ascii=False, indent=2)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert TXT to JSON")
    parser.add_argument('--input', type=str, help="Path to the input TXT file", required=True)
    parser.add_argument('--image', type=str, help="Path to the image associated with TXT annotations", required=True)
    parser.add_argument('--output', type=str, help="Path to the output JSON file", default=None)

    args = parser.parse_args()
    convert_yolo_to_labelme(args.input, args.image, args.output)
