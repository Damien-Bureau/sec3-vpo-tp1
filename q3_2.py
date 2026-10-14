import cv2
from cv2.typing import MatLike
import numpy as np

def main():
    img_gray = cv2.imread("images/peppers-128.png", cv2.IMREAD_GRAYSCALE)
    if img_gray is None:
        raise FileNotFoundError("Could not read images/peppers-128.png")
    img_resized = cv2.resize(src=img_gray,dsize=None, dst=None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
    if img_resized is None:
        raise FileNotFoundError("Error oversampling img_gray")
    
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", img_gray)
    cv2.namedWindow("Resized image")
    cv2.imshow("Resized image", img_resized)
    cv2.imwrite("images/peppers-128-resized-inter-linear.png", img_resized)


if __name__ == "__main__":
    try:
        main()
    finally:
        cv2.destroyAllWindows()
