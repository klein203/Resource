'''
@author: xusheng
'''

import cv2
import os


def stepCnt(seed):
    while True:
        yield seed
        seed += 1

global_step = stepCnt(1)

def detectEyes(roi_color, roi_gray, eye_cascade):
    # detect and draw border of eyes with green rectangle
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.03, minNeighbors=5, flags=0, minSize=(40, 40))
    
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    return len(eyes) > 0

def detectFace(frame_color, frame_gray, face_cascade, eye_cascade=None):
    # detect and draw border of face with blue rectangle
    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_color, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img=frame_color, text='Face Detected', org=(x, y-15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(127, 127, 127), thickness=1)
#         if detectEyes(frame_color[y:y+h, x:x+w], frame_gray[y:y+h, x:x+w], eye_cascade):
#             pass
#             cv2.imwrite(os.path.join('..', 'data', 'at', 'jm', 'demo.jpg'), frame_color)
#         saveAs('full_%d.jpg' % next(global_step), frame_color, size=None)
#         saveAs('%d.jpg' % next(global_step), frame_color[y:y+h, x:x+w])
    
    return len(faces) > 0

def app_run():
    face_cascade = cv2.CascadeClassifier(os.path.join('..', 'data', 'cascades', 'haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join('..', 'data', 'cascades', 'haarcascade_eye.xml'))

    camera = cv2.VideoCapture(0)
    size = (camera.get(cv2.CAP_PROP_FRAME_WIDTH), camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    while True:
        _, frame_color = camera.read()
        frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
        
        if detectFace(frame_color, frame_gray, face_cascade, eye_cascade):
            pass
#             cv2.imwrite(os.path.join('..', 'data', 'at', 'jm', 'demo.jpg'), frame_color)
            
        
        cv2.imshow(("camera_%sx%s" % (size[0], size[1])), frame_color)
        
        # ~ 12 FPS
        if cv2.waitKey(1000//12) & 0xFF == ord("q"):
            break
    
    camera.release()
    cv2.destroyAllWindows()

def saveAs(name, roi, size=(128, 128)):
    f = roi
    if size is not None:
        f = cv2.resize(roi, size)
    cv2.imwrite(os.path.join('..', 'data', 'at', 'jm', name), f)


if __name__ == '__main__':
    app_run()