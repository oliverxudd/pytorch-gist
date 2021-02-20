"""RGB & BGR order in python libraries"""

# 1. OpenCV BGR (blue-green-red)
im_bgr = cv2.imread('test.jpg')

# 2. PIL RGB (red-green-blue)
im_rgb = PIL.Image.open('test.jpg')

# 3. conversion between RGB and BRG

im_rgb = np.array(PIL.Image.open('test.jpg'))
im_bgr = cv2.cvtColor(im_rgb, cv2.COLOR_RGB2BGR)
im_bgr = im_rgb[:, :, ::-1]
