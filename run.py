#! /usr/bin/env python3

# dependencies
import pyautogui as pag # requires cv2 (opencv_python)

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

installed_path = os.path.dirname(os.path.abspath(__file__))
target_images = glob(os.path.join(installed_path, "targets", "*"))

def judge():
  for fn in target_images:
    if pag.locateOnScreen(fn, confidence=.9):
      return True
  return False

## main ##
debug.log("[[start]]")
previous_judgement = False
while True:
  judgement = judge()
  if judgement and not previous_judgement:
    on_battle_over()
  previous_judgement = judgement
  time.sleep(1)
