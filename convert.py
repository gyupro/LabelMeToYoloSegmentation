
import os
from os import walk, getcwd
from PIL import Image

def convert(size, xy):
    dw = size[0]
    dh = size[1]
    x, y = xy
    return x/dw, y/dh
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
mypath = "/home/ubuntu/datasets/cell/labels/*/*"

wd = getcwd()
#list_file = open('%s_list.txt'%(wd), 'w')

""" Get input json file list """
json_name_list = []
from glob import glob
for file in glob(mypath):
    if file.endswith(".json"):
        json_name_list.append(file)
import json

def read_name_file(name_path):
    names= []
    with open(name_path, "r") as name_file:
        for name in name_file:
            names.append(name.replace("\n", "").strip())
    return names




""" Process """
for json_name in json_name_list:
    txt_name = json_name.rstrip(".json") + ".txt"
    """ Open input text files """
    txt_path = json_name
    names = read_name_file('/home/ubuntu/datasets/cell/obj.names')

    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    
    """ Open output text files """
    txt_outpath =  txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")

    """ Convert the data to YOLO format """ 
    # lines = txt_file.read().split('\r\n')   #for ubuntu, use "\r\n" instead of "\n"
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
                
            x,y = pt
            bb = convert((width,height), [x,y])         
            txt_outfile.write(" " + " ".join([str(a) for a in bb]))
        txt_outfile.write("\n")
  
