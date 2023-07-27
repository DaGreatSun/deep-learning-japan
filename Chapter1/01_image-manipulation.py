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

################################################
# Blurring & Time Taken
################################################
# image = originalImage.copy()
# start = time.time()
# blurred = cv2.blur(image, (15, 15))
# time_blur = time.time()
# gaussian = cv2.GaussianBlur(image, (15, 15), sigmaX=15, sigmaY=15)
# time_gaussian = time.time()
# median = cv2.medianBlur(image, 15)
# time_median = time.time()
# bilateral = cv2.bilateralFilter(image, 15, 50, 50)
# time_bilateral = time.time()

# baseline = time_blur - start
# print("Blur", (time_blur - start) / baseline)
# print("Gaussian", (time_gaussian - time_blur) / baseline)
# print("Median", (time_median - time_gaussian) / baseline)
# print("Bilateral", (time_bilateral - time_median) / baseline)

################################################
# Contrast, Brightness, Gamma control
################################################
#   convertScaleAbs(reference image, image rewrite target, contrast, brightness)
################################################
# more_contrast = originalImage.copy()
# less_contrast = originalImage.copy()
# more_brightness = originalImage.copy()
# less_brightness = originalImage.copy()
# cv2.convertScaleAbs(originalImage, more_contrast, 2, 0)
# cv2.convertScaleAbs(originalImage, less_contrast, 0.5, 0)
# cv2.convertScaleAbs(originalImage, more_brightness, 1, 64)
# cv2.convertScaleAbs(originalImage, less_brightness, 1, -64)
# utils.display_concatenated(
#     "Convert Scale Abs",
#     [originalImage, more_contrast, less_contrast, more_brightness, less_brightness],
# )

# image = originalImage.copy()
# Gamma = 3
# imageGammaHigher = np.array(255 * (originalImage / 255) ** (1 / Gamma), dtype=np.uint8)
# Gamma = 0.2
# imageGammaLower = np.array(255 * (originalImage / 255) ** (1 / Gamma), dtype=np.uint8)
# utils.display_concatenated(
#     "Gamma 1.5 vs 0.5",
#     [originalImage, imageGammaHigher, imageGammaLower],
# )

################################################
# Drawing Rectangles
################################################
# poroImage = cv2.imread("poro.jpg", cv2.IMREAD_COLOR)
# cv2.rectangle(
#     poroImage, (0, 0), (poroImage.shape[1], poroImage.shape[0]), (0, 0, 255), 2
# )
# cv2.rectangle(poroImage, (140, 140), (270, 320), (0, 0, 255), 2)

# cv2.putText(poroImage, "Poro", (140, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# utils.display_concatenated("Poro", [poroImage])
