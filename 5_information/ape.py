#! /usr/bin/env python

import PIL.Image
import requests

pic = requests.get("https://mercury.picoctf.net/static/c28a959c5605d5f67480d5dd3a77f302/cat.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in pic.raw._getexif().items()
    if k in PIL.ExifTags.TAGS
}