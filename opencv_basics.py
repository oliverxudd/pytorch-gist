"""basics of OpenCV"""

# 1. add borders to image
Bsize = 2 
image = cv2.copyMakeBorder(image, top=Bsize, left=Bsize, right=Bsize, bottom=Bsize, borderType=cv2.BORDER_CONSTANT, value=0)
