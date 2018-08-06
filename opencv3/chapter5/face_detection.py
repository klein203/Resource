'''
@author: xusheng
'''

import cv2
import os

def detect():
    face_cascade = cv2.CascadeClassifier(os.path.join('..', 'data', 'cascades', 'haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join('..', 'data', 'cascades', 'haarcascade_eye.xml'))
    camera = cv2.VideoCapture(0)
    size = (camera.get(cv2.CAP_PROP_FRAME_WIDTH), camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
#     cnt = 1
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))
            
            roi_color = frame[y:y+h, x:x+w]
            roi_gray = gray[y:y+h, x:x+w]
            
            # resize POI to (200, 200), and save to disk
#             f = cv2.resize(roi_gray, (200, 200))
#             cv2.imwrite(os.path.join('..', 'data', 'at', 'jm', ('%s.pgm' % cnt)), f)
#             cnt += 1
                        
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
            
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        cv2.imshow(("camera_%sx%s" % (size[0], size[1])), frame)
        if cv2.waitKey(1000//12) & 0xFF == ord("q"):
            break
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect()