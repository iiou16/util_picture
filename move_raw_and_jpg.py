# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 05:48:48 2017

rawフォルダとjpgフォルダをカレントに作成して
指定フォルダのraw画像をrawフォルダに、jpg画像をjpgに移動する
@author: iiou1
"""

import os
import sys
import shutil

cwd = sys.argv[1]
print cwd
fn_list = os.listdir(cwd)

raw_dir = cwd + os.sep + "raw"
jpg_dir = cwd + os.sep + "jpg"

if not os.path.exists(raw_dir) :
    os.mkdir(raw_dir)
if not os.path.exists(jpg_dir) :
    os.mkdir(jpg_dir)

for fn in fn_list :
    base, ext = os.path.splitext(fn)
    if ext == ".cr2" or ext == ".CR2" :
        shutil.move(cwd+ os.sep + fn, raw_dir)
    elif ext == ".jpg" or ext == ".JPG":
        shutil.move(cwd+ os.sep + fn, jpg_dir)