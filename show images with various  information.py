import cv2

IMGPATH = "bilal.jpg"

img = cv2.imread(IMGPATH)

# show the image
cv2.imshow("bilal image",img)

# show the shape of the image
print("shape: {}".format(img.shape))  #(height,width,channel)
# show the height of the image
print("height: {}".format(img.shape[0]))
# show the width of the image
print("width : {}".format(img.shape[1]))
# show the channels of the image
print("channels: {}".format(img.shape[2]))

# save image with deferent extension
print(cv2.imwrite("bilal.png",img))

cv2.waitKey(0)
