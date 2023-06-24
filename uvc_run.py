#!/usr/bin/env python
# coding: utf-8

import cv2
import pyscreeze

# local
import debug
import secret
import notification

# standard lib
from glob import glob
import os.path
import time

def on_battle_over():
    notification.line_notify(secret.LINE_NOTIFY_TOKEN, "戦闘終了")

installed_path = "." #os.path.dirname(os.path.abspath(__file__))
target_images = list(map(cv2.imread, glob(os.path.join(installed_path, "targets", "*"))))
cap = cv2.VideoCapture(secret.UVC_NO)

def judge():
    ret, im = cap.read()
    for tim in target_images:
        if pyscreeze.locate(tim, im, confidence=.9):
            return True
    return False


# In[ ]:


## main ##
debug.log("[[start]]")
previous_judgement = False
while True:
    judgement = judge()
    if judgement and not previous_judgement:
        on_battle_over()
    previous_judgement = judgement
    time.sleep(1)

