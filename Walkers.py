import cv2


# Create our body classifier
body_classifier=cv2.CascadeClassifier("haarcascade_fullbody.xml")


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()


   
    # Capture the video frame by frame
    

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies=body_classifier.detectMultiScale(gray,1.2,3)
    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    
    
    # Extract bounding boxes for any bodies identified
    for x,y,w,h in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),3)
    
    cv2.imshow("Web cam", frame)
      

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
