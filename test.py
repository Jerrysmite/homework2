print("Hello world")

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
import shutil
import os


path = "./resources/Card/"


def template_match_fixed_location(
    image_path, template_path, fixed_loc=(124, 30), threshold=0.8
):
    image = cv.imread(image_path, 0)
    template = cv.imread(template_path, 0)

    if image is None or template is None:
        raise ValueError("Could not open or find the images.")

    result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

    value_at_fixed_loc = result[fixed_loc[1], fixed_loc[0]]

    if value_at_fixed_loc >= threshold:
        return True
    else:
        return False


def move_file(src, dest):
    try:
        # 检查源文件是否存在
        if not os.path.isfile(src):
            print(f"Source file '{src}' does not exist.")
            return False

        shutil.move(src, dest)
        print(f"File moved from '{src}' to '{dest}'")
        return True
    except Exception as e:
        print(f"Error moving file: {e}")
        return False


SSR_template_path = "./resources/template/SSR.png"
SR_template_path = "./resources/template/SR.png"
R_template_path = "./resources/template/R.png"
N_template_path = "./resources/template/N.png"

SSR_dest_dir = "./resources/SSR/"
SR_dest_dir = "./resources/SR/"
R_dest_dir = "./resources/R/"
N_dest_dir = "./resources/N/"


for items in os.scandir(path):
    image_path = items.path

    if template_match_fixed_location(image_path, SSR_template_path, (124, 30), 0.8):
        move_file(image_path, SSR_dest_dir + items.name)
    elif template_match_fixed_location(image_path, SR_template_path, (126,32), 0.8):
        move_file(image_path, SR_dest_dir + items.name)
    elif template_match_fixed_location(image_path, R_template_path, (123,34), 0.8):
        move_file(image_path, R_dest_dir + items.name)
    elif template_match_fixed_location(image_path, N_template_path, (123,40), 0.8):
        move_file(image_path, N_dest_dir + items.name)
    


# image = cv.imread(path + "UI_Card_100001.png", 0)
# template = cv.imread(N_template_path, 0)
# result = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# print(max_loc)