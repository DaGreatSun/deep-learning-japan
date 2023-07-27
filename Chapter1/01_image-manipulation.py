import cv2
import numpy as np
import time
import sys


sys.path.append("../")
import utils

originalImage = cv2.imread("test.jpg", cv2.IMREAD_COLOR)
black = np.zeros([200, 200], dtype=np.uint8)
white = np.full([200, 200], 255, dtype=np.uint8)

################################################
# Understanding Images
################################################
# print("Image Tuple (height, width, channels): ", originalImage.shape)
# print("Image Height: ", originalImage.shape[0])
# print("Image Width: ", originalImage.shape[1])
# print("Image Channel: ", originalImage.shape[2])

################################################
# Creating Images
################################################
# utils.display_multiple_window(["Black", "White"], [black, white])
# utils.display_concatenated("images", [black, white])

################################################
# Rows and Columns
################################################
# blackAlter = black.copy()
# blackAlter[90:120, 90:120] = white[90:120, 90:120]
# blackAlter[:, 20:40] = 100
# utils.display_concatenated("Copy Region of Interest", blackAlter)

################################################
# Converting Color Images
################################################
# imageGreyscaled = cv2.cvtColor(originalImage.copy(), cv2.COLOR_RGB2GRAY)
# utils.display_concatenated("Copy Region of Interest", imageGreyscaled)
# utils.display_concatenated("Copy Region of Interest", cv2.flip(imageGreyscaled, 1))

################################################
# Chequered Board
################################################
# row1 = cv2.hconcat([black, white, black, white])
# row2 = cv2.hconcat([white, black, white, black])
# row3 = cv2.hconcat([black, white, black, white])
# row4 = cv2.hconcat([white, black, white, black])
# utils.display_concatenated("Chequered Board", [row1, row2, row3, row4], "v")
