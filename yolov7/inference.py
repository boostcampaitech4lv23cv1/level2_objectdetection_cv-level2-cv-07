import cv2
import torch
import json
import pandas as pd
from PIL import Image
from tqdm import tqdm
import argparse
import os

def inference(experience_name, iou=0.5):
    dataset_root = '../dataset/test/'

    model = torch.hub.load('./', 'custom', path_or_model= f'./runs/train/{experience_name}/weights/best.pt', source='local') 
    model.conf = 0.001  # confidence threshold (0-1)
    model.iou = iou  # NMS IoU threshold (0-1)

    prediction_string = ['']  * 4871 
    image_id = [f'test/{i:04}.jpg' for i in range(4871)]
    for i in tqdm(range(4871)):
        img = Image.open(os.path.join(dataset_root, f'{i:04}.jpg'))

        results = model(img, size=1280, augment=True)
        for bbox in results.pandas().xyxy[0].values:
            xmin, ymin, xmax, ymax, confidence, clss, name = bbox
            prediction_string[i] += f'{clss} {confidence} {xmin} {ymin} {xmax} {ymax} '
    raw_data ={
        'PredictionString' : prediction_string,
        'image_id' : image_id
    }
    dataframe = pd.DataFrame(raw_data)

    # runs/train/yolov7/exp_name에 저장
    dataframe.to_csv(f'./runs/train/{experience_name}/submission_{iou}.csv', sep=',', na_rep='NaN', index=None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='inference.py')
    parser.add_argument('--exp', nargs='+', type=str, default='yolov7-e6e4', help='model.pt path(s)')
    opt = parser.parse_args()

    inference(opt.exp)

