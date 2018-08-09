'''
@author: xusheng
'''

import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.EmbossFilter()
    
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # filter the frame
#             frame = cv2.GaussianBlur(frame, (3, 3), 0)
#             self._captureManager._frame = cv2.Canny(frame, 50, 150)
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvent()
            
    def onKeypress(self, keycode):
        if keycode == 32:   # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == '__main__':
    Cameo().run()