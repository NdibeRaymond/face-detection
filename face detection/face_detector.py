import cv2
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\user\Pictures\Camera Roll\WP_20151129_011.jpg")
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray_image,scaleFactor = 1.5,minNeighbors = 5)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)


cv2.imshow("faces",cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3))))
cv2.waitKey(0)
cv2.destroyAllWindows()
