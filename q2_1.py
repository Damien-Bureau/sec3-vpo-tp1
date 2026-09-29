import cv2
import matplotlib.pyplot as plt

def histo(img_gray) -> None:
    # Compute histogram
    hist = cv2.calcHist(images=[img_gray],
                        channels=[0],
                        mask=None,
                        histSize=[256],
                        ranges=[0,256])

    # Plot histogram
    plt.hist(img_gray.ravel(), 256, [0,256])
    # plt.plot(hist)
    plt.xlabel("Gray levels [0-255]")
    plt.ylabel("Number of pixels")

if __name__ == "__main__":
    # Load image in grayscale
    img_gray = cv2.imread("images/peppers-512.png", cv2.IMREAD_GRAYSCALE)
    histo(img_gray)
    
    plt.show()
