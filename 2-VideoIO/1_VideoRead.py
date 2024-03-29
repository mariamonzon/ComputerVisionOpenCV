# Import module
import cv2
from dataPath import DATA_PATH

video = cv2.VideoCapture('../data/videos/chaplin.mp4')

# Check if camera opened successfully
if (video.isOpened()== False):
  print("Error opening video stream or file")

while(video.isOpened()):
  # Capture frame-by-frame
  ret, frame = video.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press esc on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == 27:
      break

  # Break the loop
  else:
    break
