import cv2
import numpy as np
from sqlalchemy import true
from otherfuns import findsize
def createBlack(height, width):
  img = np.zeros((height,width, 3),dtype=np.uint8)
  for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        img[j,i]=0
  return img
# Create a VideoCapture object and read from input file
caps = []
for i in range(0, 10):
  caps.append(cv2.VideoCapture("vid" + str(i + 1) + ".mp4"))

# Check if camera opened successfully

# Read until video is completed
oneblack = createBlack(720, 1280)
size = 10
fakearr = findsize(size)
arr = []
for i in fakearr:
  blackbegone = True
  for j in i:
    if j:
      blackbegone = False
  if not blackbegone:
print(arr)
while(caps):
#2560 by 1440
  # Capture frame-by-frame
  rets = []
  frames = []
  for i in caps:
    ret, frame = i.read()
    rets.append(ret)
    frames.append(frame)
  if rets:
    curframe = ""
    counter = 0
    for i in arr:
      thingy = ""
      for j in i:
        if thingy == "":
          if j == ".":
            thingy = frames[counter]
            counter += 1
          else:
            thingy = oneblack
        else:
          if j == ".":
            thingy = cv2.hconcat([thingy, frames[counter]])
            counter += 1
          else:
            thingy = cv2.hconcat([thingy, oneblack])
      if curframe == "":
        curframe = thingy
      else:
        curframe = cv2.vconcat([curframe, thingy])
        

    imS = cv2.resize(curframe, (3840, 1440))

    # Display the resulting frame
    cv2.imshow('Frame', imS)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else: 
    break
# When everything done, release 
# the video capture object
cap.release()
cap2.release()

# Closes all the frames
cv2.destroyAllWindows()