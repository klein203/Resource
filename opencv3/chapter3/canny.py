'''
@author: xusheng
'''

import cv2
import os

if __name__ == '__main__':
    img = cv2.imread(os.path.join('..', 'data', 'koala.jpg'), 0)
    img = cv2.Canny(img, 200, 300)
    channels = cv2.split(img)
    for channel in channels:
        channel[:] = 255 - channel
    cv2.merge(channels, img)
    cv2.imwrite('koala_canny.jpg', img)
    cv2.imshow('canny', cv2.imread('koala_canny.jpg'))
     
    cv2.waitKey()
    cv2.destroyAllWindows()

#     img = cv2.imread('avator_2.jpg', 0)
#     img = cv2.GaussianBlur(img, (3, 3), 0)
#     img = cv2.Canny(img, 50, 100)
#     channels = cv2.split(img)
#     for channel in channels:
#         channel[:] = 255 - channel
#     cv2.merge(channels, img)
#     cv2.imwrite('avator_2_canny.jpg', img)
