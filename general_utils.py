import cv2
import matplotlib.pyplot as plt


def display_multiple_window(name, images):
    images = images if isinstance(images, list) else [images]
    name = (
        name
        if isinstance(name, list)
        else [str(name) + " " + str(element) for element in range(len(images))]
    )

    if len(name) != len(images):
        print("Name and images has different lengths")
        print("Number of Names ", len(name))
        print("Number of Images ", len(images))
        return -1

    for index, image in enumerate(images):
        cv2.imshow(name[index], images[index])

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

    return images


def display_concatenated(name, images, alignment="h"):
    if alignment == "v":
        images = cv2.vconcat(images) if isinstance(images, list) else images
    else:
        images = cv2.hconcat(images) if isinstance(images, list) else images

    cv2.imshow(name, images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return images


def save_images(path, name, images):
    images = images if isinstance(images, list) else [images]

    if len(images) == 1:
        cv2.imwrite(path + "/" + name + ".jpg", images[0])
    else:
        for index, image in enumerate(images):
            cv2.imwrite(path + "/" + name + str(index + 1) + ".jpg", image)


def mathplot_display_concatenated(name, images, alignment="h"):
    if alignment == "v":
        images = cv2.vconcat(images) if isinstance(images, list) else images
    else:
        images = cv2.hconcat(images) if isinstance(images, list) else images

    plt.imshow(cv2.cvtColor(images, cv2.COLOR_BGR2RGB))

    return images
