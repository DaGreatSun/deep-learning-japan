import cv2
import numpy as np
import time
import sys

sys.path.append("../")
import utils

originalImage = cv2.imread("pedestrian-detection/street.jpg", cv2.IMREAD_COLOR)

# Prepare the hog detector to detect pedestrians
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(boxes, weights) = hog.detectMultiScale(
    originalImage, winStride=(4, 4), padding=(2, 2), scale=1.05, hitThreshold=0
)

print(boxes, weights)

for index, (x, y, w, h) in enumerate(boxes):
    cv2.rectangle(originalImage, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(
        originalImage,
        "Pedestrian" + str(index + 1),
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )

utils.display_multiple_window("pedestrians", [originalImage])
utils.save_images("pedestrian-detection", "street-detected", [originalImage])
