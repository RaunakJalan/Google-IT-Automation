#!/usr/bin/env python3

import os

from PIL import Image

newsize = 128, 128

def fixImageSave(files,dir):
        for file in files:
                if "ic" in file:
                        im = Image.open(dir+file).convert('RGB')

                        im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")

def filenames(dir):
        files = []
        for (dirpath, dirname, filenames) in os.walk(dir):
                files.extend(filenames)
                break

        fixImageSave(files,dir)


filenames("images/")





