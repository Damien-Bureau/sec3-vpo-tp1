import cv2
import matplotlib.pyplot as plt

from q2_1 import histo


def main():
    img_gray = cv2.imread("images/peppers-512.png", cv2.IMREAD_GRAYSCALE)
    img_gray_equalized = cv2.equalizeHist(img_gray)
    histo(img_gray)
    histo(img_gray_equalized)
    
    cv2.namedWindow("Original image")
    cv2.imshow("Original image", img_gray)
    cv2.namedWindow("Equalized image")
    cv2.imshow("Equalized image", img_gray_equalized)
    cv2.imwrite("images/peppers-512-eq.png", img_gray_equalized)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    finally:
        cv2.destroyAllWindows()
