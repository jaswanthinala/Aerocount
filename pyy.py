import cv2

img = cv2.imread("pic.jpg")  # Load an image
cv2.imshow("Image", img)  # Display the image

cv2.waitKey(0)  # Wait for a key press indefinitely
cv2.destroyAllWindows()  # Close the image window
