import cv2

# Load the original image
original_img = cv2.imread('D:\IDM downloads\Documents\IUT Textbook 7th Semester\DIP\Sessional\Image Set\color1.jpg')
# Load an image in grayscale, 0 as the second parameter.
grayscale_img = cv2.imread('D:\IDM downloads\Documents\IUT Textbook 7th Semester\DIP\Sessional\Image Set\color1.jpg', 0)
cv2.imshow('Beauty', grayscale_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the gray scale image
cv2.imwrite('grayBeauty.jpg', grayscale_img)
