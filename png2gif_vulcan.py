# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 05:45:30 2021

@author: birnb
"""

import PIL
from PIL import Image, ImageMath
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
import numpy as np
import pandas as pd

url = 'http://vulcan1.ldeo.columbia.edu/vulcand/ldeo/raw/data/siteCv/IrCam2/PalmaImgSiteCv2021-11/'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

df = pd.DataFrame({'png':soup.find_all('a')})
df = df.loc[df.png.apply(lambda x: 'Palma' in str(x))]
df['month'] = df.png.apply(lambda x: str(x).split('_')[0].split('-')[-2])
df['day'] = df.png.apply(lambda x: str(x).split('_')[0].split('-')[-1])
df['hr'] = df.png.apply(lambda x: int(str(x).split('_')[-1].split('-')[0][0:2]))
df['m'] = df.png.apply(lambda x: int(str(x).split('_')[-1].split('-')[0][2:4]))
df['sec'] = df.png.apply(lambda x: int(str(x).split('_')[-1].split('-')[0][4:6]))
df['time_num'] = df.hr*3600 + df.m*60 + df.sec
gb = df.groupby('day')

for group in gb: 
    gif = []
    
    for hr in group[1].groupby('hr'):
        dat = hr[1].sort_values('m')
    
        for i, d in df.iterrows():
            png_name = d.png.get('href')
            if '00001' in png_name:
                img = Image.open(urlopen(url + png_name))
                img2 = ImageMath.eval('img/256', {'img':img}).convert('RGB')
                gif.append(img2)
                if (len(gif)%20==0):
                    print(str(len(gif)) + ' frames loaded')
                    print('time = ' + str(d.hr) + ':' +  str(d.m) + ':' + str(d.sec))
        gif[0].save('11-' + group[0]  + '-' + hr[0] + '.gif', save_all=True,optimize=False, append_images=gif[1:], loop=0, duration=48)