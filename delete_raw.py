# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 05:43:54 2017

@author: iiou16
カレントの直下にrawフォルダとjpgフォルダがある前提

jpgしかない画像はカレントにコピー
rawしかない画像はrawを失敗フォルダへ移動

先にjpg画像で必要な画像を確認して、いらない画像を削除してから実行するスクリプト
"""

import os
import sys
import shutil

ext_raw = ".CR2"
ext_jpg = ".JPG"

def get_base(fn) :
    base, ext = os.path.splitext(fn)
    return base

cwd = sys.argv[1]

raw_dir = cwd + os.sep + "raw"
jpg_dir = cwd + os.sep + "jpg"
not_use_dir = cwd + os.sep + "not_use"

if not os.path.exists(raw_dir) or not os.path.exists(jpg_dir) :
    print("error : need ./raw & ./jpg dir.")
    exit()

raw_list = os.listdir(raw_dir)
raw_list = map(get_base, raw_list)
raw_set= set(raw_list)
jpg_list = os.listdir(jpg_dir)
jpg_list = map(get_base, jpg_list)
jpg_set = set(jpg_list)

only_raw = raw_set.difference(jpg_set)
only_jpg = jpg_set.difference(raw_set)

for raw in only_raw :
    if not os.path.exists(not_use_dir) :
        os.mkdir(not_use_dir)
    raw_fn = raw + ext_raw
    #os.remove(raw_dir + os.sep + raw_fn)
    shutil.move(raw_dir + os.sep + raw_fn, not_use_dir)

for jpg in only_jpg :
    jpg_fn = jpg + ext_jpg
    shutil.copy2(jpg_dir + os.sep + jpg_fn, cwd)

