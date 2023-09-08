# LabelMeToYoloSegmentation
Convert labelme format to yolo segmentation format

Now, you can convert back yolo segmentation format to labelme format

Usage

### labelme2yolo
```bash
python labelme2yolo.py --input /path/to/input.json --output /path/to/output.txt
```

### yolo2labelme
You need create obj.names file that defines your cls 

```bash
python yolo2labelme.py --input /path/to/input.txt --image /path/to/image.jpg --output /path/to/output.json
```

Convert segmentation created by labelme format to Yolo Segmentation format

![image](https://user-images.githubusercontent.com/79894531/214529150-ca61e5f5-6336-4546-bbf9-8f576c4232a5.png)

![image](https://user-images.githubusercontent.com/79894531/214529172-15b51a6c-769f-4caf-be8c-6595739ad966.png)

## obj.names example  
![image](https://user-images.githubusercontent.com/79894531/214529306-1eaa410e-9804-4030-a67d-40a4a4e4ce52.png)

