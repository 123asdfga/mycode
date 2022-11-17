#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:00:09 2021

@author: ubuntu
"""
import numpy
from PIL import Image, ImageDraw, ImageFont
import cv2

def cv2ImgAddText(img, text, left, top, textColor=(255, 0, 0), textSize=20):

    if (isinstance(img, numpy.ndarray)):  #判断是否OpenCV图片类型

        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(img)

    fontText = ImageFont.truetype(

        "./simhei.ttf", textSize, encoding="utf-8")

    draw.text((left, top), text, textColor, font=fontText)

    return  cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


img = "528.jpg"

text = '违规抛物！'

img1 = cv2.imread(img)

cv2ImgAdd