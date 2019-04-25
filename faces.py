import face_recognition as fr
import cv2

img1=fr.load_image_file("/home/kobra/Desktop/nag1.jpg")
fe1=fr.face_encodings(img1)

cam=cv2.VideoCapture(0)
while(1):
    r,i=cam.read()
    
    imgcheck=i
    
    fl=fr.face_locations(imgcheck)
    print(fl)
    fecheck=fr.face_encodings(imgcheck,fl)
    if len(fl)>0:
        fm=fr.compare_faces(fe1,fecheck[0])
        print(fm)


    
    for x in range(len(fl)):
        cv2.rectangle(i,(fl[x][3],fl[x][0]),(fl[x][1],fl[x][2]),(0,255,0),5)
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if k==ord('y'):
        cv2.destroyAllWindows()
        break
        
cam.release()

