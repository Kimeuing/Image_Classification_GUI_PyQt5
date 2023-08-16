#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
from torch import nn as nn
import torch.nn.functional as F
from torch import optim
import numpy as np
import torchvision
import torchvision.transforms as transforms
from tqdm.auto import tqdm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import os
import cv2
import pandas as pd 
from torchvision.models.resnet import resnet50


def run(folder_name,mode):
    
    image_list_ = folder_name
    pathmode = mode
    t_model = torch.load(pathmode)
    classes = ["불량 유형 1","불량 유형 3","불량 유형 2"]
    trans = transforms.Compose([transforms.Resize((256,256)),
                            transforms.Grayscale(num_output_channels=1),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5,),(0.5,))
                           ])
    x = []

    def img_pred(img_path):
        image = Image.open(img_path)
        img = trans(image)
        pred_num = int(np.squeeze(t_model(img.unsqueeze(0).cuda()).data.max(1, keepdim=True)[1].cpu().numpy()))
        pred_name = classes[pred_num]
        return x.append(pred_name)
    files = os.listdir(folder_name)
    image_list_tif= [file for file in files if not file.endswith("(ER).tif")]
    image_error_tif=[file for file in files if file.endswith("(ER).tif")]
    df = pd.DataFrame(image_list_tif, columns=['a'])
    real_image_list_tif = []
    for i in range(len(image_list_tif)):
        real_image_list_tif.append(image_list_tif[i][image_list_tif[i].find("(")+1:image_list_tif[i].find(")")])

    df['b'] = real_image_list_tif
    df = df.astype({'b':'float'})

    df1 = df[df['b']<0.0015]
    df2 = df[df['b']>=0.0015]
    image_pass_tif = df1['a'].to_list()                                           
    image_ng_tif = df2['a'].to_list()
    for i in range(len(image_ng_tif)):
        img_pred(f"{folder_name}/{image_ng_tif[i]}")
    
        fig = plt.figure()
   
        
    for i in range(len(image_ng_tif)):
        img_array = np.fromfile(f"{folder_name}/{image_ng_tif[i]}",np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        ax = fig.add_subplot(1000,1000,i+1)
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_xlabel(x[i])
        ax.set_xticks([]), ax.set_yticks([])
        breaks = x.count('불량 유형 1')
        foreigns = x.count('불량 유형 3')
        waves= x.count('불량 유형 2')
        y = x
        
        
    return breaks, foreigns, waves, y


