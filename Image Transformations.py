import cv2
import numpy as np

# For putting text on images
# font
font = cv2.FONT_HERSHEY_SIMPLEX

# origin
org = (50, 50)

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

"""
Negative Image Transformation to Grayscale (https://theailearner.com/2019/01/01/image-negatives/)
"""
# Load the basic image
img1 = cv2.imread('Fig3.27(a).jpg')
# Check the datatype of the image
print(img1.dtype)
# Subtract the img1 from max value(calculated from dtype)
img1_neg = 255 - img1
# Show the image
cv2.imshow('Negative image', img1_neg)
cv2.waitKey(0)

"""
Power-Law Transformation
"""
img2 = cv2.imread('Fig3.08(a).jpg')
# Apply Gamma=2.2 on the normalised image and then multiply by scaling constant (For 8 bit, c=255)
gamma_level_greater_than_one = 2.2
darker_img = np.array(255 * (img2 / 255) ** gamma_level_greater_than_one, dtype='uint8')
darker_img = cv2.putText(darker_img, 'Gamma Level : ' + str(gamma_level_greater_than_one), org, font, fontScale, color,
                         thickness, cv2.LINE_AA)

# Similarly, Apply Gamma=0.4
gamma_level_less_than_one = 0.4
brighter_img = np.array(255 * (img2 / 255) ** 0.4, dtype='uint8')
brighter_img = cv2.putText(brighter_img, 'Gamma Level : ' + str(gamma_level_less_than_one), org, font, fontScale, color,
                           thickness, cv2.LINE_AA)

# Display the images in subplots
result_img = cv2.hconcat([darker_img, brighter_img])
# Show the image
cv2.imshow('Gamma Picture', result_img)
cv2.waitKey(0)

"""
Negative of color image
"""
img3 = cv2.imread('color1.jpg')
# Check the datatype of the image
print(img3.dtype)
print(img3.shape)
# Subtract the img from max value(calculated from dtype)
img3_neg = 255 - img3
# Show the image
cv2.imshow('Neg Color Image', img3_neg)
cv2.waitKey(0)
