import cv2
import numpy as np

# Load the image
image = cv2.imread('day3/Candies.png')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for blue color in HSV
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Create a mask for blue color
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Extract the blue candies using the mask
blue_candies = cv2.bitwise_and(image, image, mask=mask)

# Display the result
cv2.imshow('Blue Candies', blue_candies)
cv2.waitKey(0)
cv2.destroyAllWindows()