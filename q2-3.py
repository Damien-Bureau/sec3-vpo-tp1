import cv2
import matplotlib.pyplot as plt

from q2_1 import histo


def main():
    img_gray = cv2.imread("images/peppers-512.png", cv2.IMREAD_GRAYSCALE)
    img_gray_luminosity = cv2.convertScaleAbs(img_gray, alpha=1, beta=40)
    img_gray_contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)
    histo(img_gray)
    # histo(img_gray_luminosity)
    histo(img_gray_contrast, "green")
    
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", img_gray)
    cv2.namedWindow("Increased luminosity")
    cv2.imshow("Increased luminosity", img_gray_luminosity)
    cv2.imwrite("images/peppers-512-luminosity.png", img_gray_luminosity)
    cv2.namedWindow("Increased contrast")
    cv2.imshow("Increased contrast", img_gray_contrast)
    cv2.imwrite("images/peppers-512-contrast.png", img_gray_contrast)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    finally:
        cv2.destroyAllWindows()
