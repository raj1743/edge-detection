import cv2
import numpy as np

# Reading the image in GrayScale
image = cv2.imread('photo-1.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel Operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Scharr Operator
scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharr_combined = cv2.magnitude(scharr_x, scharr_y)

# Smoothing the image for Canny Edge Detection
image_smoothed = cv2.GaussianBlur(image, (5, 5), 0)
laplacian = cv2.Laplacian(image_smoothed, cv2.CV_64F)

canny = cv2.Canny(image, threshold1=100, threshold2=200)

# Displaying all the images
cv2.imshow('Sobel', sobel_combined.astype(np.uint8))
cv2.imshow('Scharr', scharr_combined.astype(np.uint8))
cv2.imshow('LoG', laplacian.astype(np.uint8))
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
