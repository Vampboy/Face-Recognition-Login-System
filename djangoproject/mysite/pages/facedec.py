import os
from django.urls import path, include
import face_recognition
import cv2 
# initialize the camera
def facedect(loc):
        cam = cv2.VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        if s:    # frame captured without any errors
                cv2.namedWindow("cam-test")
                cv2.imshow("cam-test",img)
                #cv2.waitKey(0)
                cv2.destroyWindow("cam-test")
                cv2.imwrite("filename.jpg",img)

                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                MEDIA_ROOT =os.path.join(BASE_DIR,'pages')

                print(MEDIA_ROOT,loc)
                loc=(str(MEDIA_ROOT)+loc)
                print(loc)
                print("/home/light/codes/web/djangoproject/mysite/pages/media/profil_images/IMG_20180330_1600482-01.jpg")
                face_1_image = face_recognition.load_image_file(loc)
                face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

                #

                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)

                print(check)
                if check[0]:
                        return True

                else :
                        return False    

facedect('/media/profil_images/IMG_20180330_1600482-01.jpg')