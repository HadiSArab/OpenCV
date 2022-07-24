import numpy as np
import cv2

ali = np.zeros((680,680,3),np.uint8)
ali[:] = 150,100,255
print(ali.shape)
cv2.imshow("pic",ali)
cv2.waitKey(0)