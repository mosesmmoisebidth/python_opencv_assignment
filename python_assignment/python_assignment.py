import cv2 as cv

image = cv.imread('sample_image.jpg')

overlay = image.copy()
cv.rectangle(overlay, (893, 97), (1120, 177), (0, 0, 0), -1)
alpha = 0.7
cv.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
cv.rectangle(image,(260,180),(990,932),(0,255,0),5)
cv.putText(image, "RAH972U", (900, 160), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
cv.imshow('Image Result', image)
cv.imwrite('sample_image_result.jpg', image)
cv.waitKey(0)
cv.destroyAllWindows()
