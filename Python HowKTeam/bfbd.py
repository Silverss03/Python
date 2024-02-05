import cv2
img_location = r'D:\Code\bf.png'
img = cv2.imread(img_location)
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image= 255 - gray_img
blurred_img= cv2.GaussianBlur(inverted_gray_image,(21,21),0)
inverted_blurred_img=255- blurred_img
pencil_sketch_img= cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
cv2.imshow('My fiend', img)
cv2.imshow('Not My fiend', pencil_sketch_img)
cv2.waitKey(0)