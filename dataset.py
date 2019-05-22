import cv2
import os,sqlite3
cam = cv2.VideoCapture(0) #video capture with camera 0
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
face_detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
name=input("Enter the name: ")
cid = input("Enter the CID number: ")
gender = input("Enter the gender: ")
designation = input("Enter the designation: ")

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        image_path = "dataset/User." + str(face_id) + '.' + str(count) + ".jpg"
        cv2.imshow('image', img)
        if count is 25:
            connection = sqlite3.connect('mySSS.db')
            cur = connection.cursor() 
            cur.execute('''INSERT INTO Person(name,cid,designation,gender,imagePath) VALUES(?,?,?,?,?)''',(name,cid,designation,gender,image_path,))
            connection.commit()
            connection.close()
        count += 1
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()