import cv2
import numpy as np

# Load the image
image = cv2.imread('day3/mountain.jpg', cv2.IMREAD_COLOR)

# Check if image is loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Apply average filter
kernel_size = (5, 5)
average_filtered = cv2.blur(image, kernel_size)

# Apply sharpening filter
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

# Apply Laplacian filter
laplacian_filtered = cv2.Laplacian(image, cv2.CV_64F)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Average Filter', average_filtered)
cv2.imshow('Sharpening Filter', sharpened)
cv2.imshow('Laplacian Filter', laplacian_filtered)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()