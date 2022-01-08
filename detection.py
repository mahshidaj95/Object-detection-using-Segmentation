import cv2
 
#Path of image
image = cv2.imread("1.jpg")
new_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
 
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)
 
inverted_binary = ~binary
 

contours, hierarchy = cv2.findContours(inverted_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     

with_contours = cv2.drawContours(image, contours, 1, (255,0,255),3)
 
 
x, y, w, h = cv2.boundingRect(contours[0])

bounding_boxes = []

for c in contours:
  x, y, w, h = cv2.boundingRect(c)
 
    # To avoid drawing bounding box inner of each coffe bean, we should increase number of cv2.contourArea(c)) in below:
    # For example we can increase 3000:
  if (cv2.contourArea(c)) > 5000:
    cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)
    coordinate = (x, y, w, h)
    bounding_boxes.append(coordinate)


cv2.imwrite("result.jpg", with_contours)

#Path of image
image2 = cv2.imread("1.jpg")
num = 1
for box in bounding_boxes:
    x,y,w,h = box
    ROI = image2[y:y+h, x:x+w]
    cv2.imwrite('ROI_{}.jpg'.format(num), ROI)
    num += 1



