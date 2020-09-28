import cv2 as cv
import numpy as np 
import imutils
import argparse
from CamThread import WebcamVideoStream

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

vs = WebcamVideoStream(src="MVI_3736.mov").start()

# loop over some frames...this time using the threaded stream
try:
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		
		# check to see if the frame should be displayed to our screen
		if args["display"] > 0 and vs.grabbed:
			frame = imutils.resize(frame, width=400)
			shapeMask = cv.inRange(frame, (150,150,150), (230,220,220))
			cnts = cv.findContours(shapeMask.copy(), cv.RETR_EXTERNAL,
				cv.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)
			
			cv.imshow("Mask", shapeMask)
			# loop over the contours
			# draw the contour and show it
			cv.drawContours(frame, cnts, -1, (0, 255, 0), 2)
			cv.imshow("Image", frame)

			#second pass
			average = frame.mean(axis=0).mean(axis=0)
			threshold = cv.inRange(frame, average, (255,255,255))
			threshold.shape = ((225,400,1))
			
			frame = threshold - (threshold * frame)
			
			kernel = np.ones((2,2),np.uint8)
			opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
			erode = cv.erode(frame, kernel)
			cv.imshow("Frame", frame)
			cv.imshow("Erode", erode)
			cv.imshow("Clear", opening)
			key = cv.waitKey(1) & 0xFF
		# update the FPS counter
	# stop the timer and display FPS information
	# do a bit of cleanup
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
cv.destroyAllWindows()
vs.stop()