import cv2
import numpy as np

def compare_images():
    img1 = input("Enter the first image file name: ")
    img2 = input("Enter the second image file name: ")
    a = cv2.imread(img1)
    b = cv2.imread(img2)
    difference = cv2.subtract(a, b)    
    result = not np.any(difference)
    if result is True:
        print("Pictures are the same")
    else:
        cv2.imwrite("difference.png", difference )
        print("Pictures are different, the difference is stored as ed.png")