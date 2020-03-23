from django.conf import settings

import os
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 


def convert_image(filename):
    path_to_image = os.path.join(settings.MEDIA_ROOT, filename)
    edited_name = filename.split('.')
    edited_name = edited_name[0]+'-edited.'+edited_name[1]
    try:
        color_image = Image.open(path_to_image)
        bw = color_image.convert('L')
        bw.save(os.path.join(settings.MEDIA_ROOT, edited_name))
        return edited_name
    except:
        return False 