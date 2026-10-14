import cv2
from cv2.typing import MatLike
import numpy as np


def downsample(image: MatLike, factor: int) -> MatLike:
    img_width = image.shape[0]
    img_height = image.shape[1]
    # resized_img = np.zeros(shape=(int(img_height/factor), int(img_width/factor)), dtype=np.uint8)
    resized_img = np.zeros(shape=(int(img_width/factor), int(img_height/factor)), dtype=np.uint8)
    for y in range(0, img_height, factor):
        for x in range(0, img_width, factor):
            # compute average pixel corresponding to block of size "factor"
            average_pixel: int = 0
            for y_block in range(factor):
                for x_block in range(factor):
                    average_pixel += int(image[y+y_block][x+x_block])
            average_pixel = int(average_pixel/factor**2)
            
            # write average pixel in new image
            resized_img[int(y/factor)][int(x/factor)] = average_pixel
    return resized_img


def main():
    img_gray = cv2.imread("images/peppers-256.png", cv2.IMREAD_GRAYSCALE)
    if img_gray is None:
        raise FileNotFoundError("Could not read images/peppers-256.png")
    # img_resized = downsample(image=img_gray, factor=4)
    img_resized = cv2.resize(src=img_gray,dsize=None, dst=None, fx=1/4, fy=1/4, interpolation=cv2.INTER_AREA)
    if img_resized is None:
        raise FileNotFoundError("Error downsampling img_gray")
    
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", img_gray)
    cv2.namedWindow("Resized image")
    cv2.imshow("Resized image", img_resized)
    cv2.imwrite("images/peppers-256-resized-inter-area.png", img_resized)


if __name__ == "__main__":
    try:
        main()
    finally:
        cv2.destroyAllWindows()
