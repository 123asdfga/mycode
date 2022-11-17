#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:41:49 2022

@author: ubuntu
"""
import json
with open("/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/coco/test.json",'rb') as f:
    file = json.load(f)
    print(file)