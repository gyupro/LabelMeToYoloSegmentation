
import json


def read_name_file(name_path):
    names = []
    with open(name_path, "r") as name_file:
        for name in name_file:
            names.append(name.replace("\n", "").strip())
    return names

def convert_coor(size, xy):
    dw = size[0]
    dh = size[1]
    x, y = xy
    return x / dw, y / dh
def convert(file, txt_name=None):

    if txt_name is None:
        txt_name = file.rstrip(".json") + ".txt"
    """ Open input text files """
    txt_path = file
    names = read_name_file('obj.names')

    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")

    """ Open output text files """
    txt_outpath = txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")

    """ Convert the data to YOLO format """
    js = json.loads(txt_file.read())

    for item in js["shapes"]:
        label = item["label"]
        for i, name in enumerate(names):
            if label == name:
                cls = str(i)

        height = js["imageHeight"]
        width = js["imageWidth"]
        point = item["points"]

        for idx, pt in enumerate(point):
            if idx == 0:
                txt_outfile.write(cls)

            x, y = pt
            bb = convert_coor((width, height), [x, y])
            txt_outfile.write(" " + " ".join([str(a) for a in bb]))
        txt_outfile.write("\n")



