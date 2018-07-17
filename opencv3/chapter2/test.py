'''
@author: xusheng
'''

import cv2
import numpy as np
import os
from six.moves import xrange

height = 768
width = 1024
channel = 3

def _load_img(name='koala.jpg', config=cv2.IMREAD_UNCHANGED):
    img = cv2.imread(os.path.join('..', 'data', name), config)
    return img

def _save_as_png(name, img):
    cv2.imwrite(os.path.join('.', name), img)

def imgread_configs_demo():
    configs = [cv2.IMREAD_ANYCOLOR, cv2.IMREAD_ANYDEPTH, cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_LOAD_GDAL, cv2.IMREAD_UNCHANGED]
    img_suffixs = ['koala_anycolor.png', 'koala_anydepth.png', 'koala_color.png', 'koala_grayscale.png', 'koala_load_gdal.png', 'koala_unchanged.png']
    for i in xrange(len(configs)):
        img = _load_img(name='koala.jpg', config=configs[i])
        _save_as_png(img_suffixs[i], img)

def convert_img_demo():
    byte_array = bytearray(_load_img())
    bgr_img = np.array(byte_array).reshape(height*2, int(width/2), channel)
    _save_as_png('koala_convert.png', bgr_img)

def random_img_demo():
    random_img = np.random.randint(0, 256, height * width * channel).reshape(height, width, channel)
    _save_as_png('sample_random.png', random_img)

def bulk_fill_demo():
    img = _load_img()
    h_from = int((height-100)/2)
    h_to = int((height+100)/2)
    w_from = int((width-100)/2)
    w_to = int((width+100)/2)
    img[h_from:h_to, w_from:w_to] = [255, 255, 255]
    _save_as_png('koala_bulk_fill.png', img)

def save_video_demo():
    # Wildlife.wmv is a 30s video with wmv format, about 25 MB
    video_capture = cv2.VideoCapture(os.path.join('..', 'data', 'Wildlife.wmv'))
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    # convert to I420 avi, about 1.2 GB
    video_writer = cv2.VideoWriter('output_wildlife.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
    
    success, frame = video_capture.read()
    while success:
        video_writer.write(frame)
        success, frame = video_capture.read()

def save_camera_demo():
    camera_capture = cv2.VideoCapture(0)
    seconds = 5
    fps = 20
    size = (int(camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    video_writer = cv2.VideoWriter('output_camera.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
    
    success, frame = camera_capture.read()
    num_frame_remaining = seconds * fps - 1
    while success and num_frame_remaining > 0:
        video_writer.write(frame)
        success, frame = camera_capture.read()
        num_frame_remaining -= 1
    camera_capture.release()

def show_img_demo():
    img = _load_img('koala.png')
    cv2.imshow('koala', img)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

def camera_window_demo():
#     clicked = False
    def onMouse(event, x, y, flags, param):
#         global clicked
        if event == cv2.EVENT_LBUTTONUP:
#             clicked = True
            print('EVENT_LBUTTONUP @(%s, %s)' % (x, y))
    
    camera_capture = cv2.VideoCapture(0)
    cv2.namedWindow('CameraWindow')
    cv2.setMouseCallback('CameraWindow', onMouse)
    
    success, frame = camera_capture.read()
    while success and cv2.waitKey(1) == -1:
        cv2.imshow('CameraWindow', frame)
        success, frame = camera_capture.read()
    cv2.destroyWindow('CameraWindow')
    camera_capture.release()
    

def main():
    camera_window_demo()

if __name__ == '__main__':
    main()