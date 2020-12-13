# %%
# NOTE: imported as such to disable linting errors due to C headers
from cv2 import cv2 as cv
# Location of cascades used for object detection
from cv2.data import haarcascades
import os
# %%
def face_detect(frame, face_cascade=cv.CascadeClassifier()):
	"""detect a face in a frame and draw a bounding box"""
	frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	frame_gray = cv.equalizeHist(frame_gray)

	faces = face_cascade.detectMultiScale(frame_gray)
	#print(len(faces))
	for (x, y, w, h) in faces:
		frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)

	return frame


# %%
def get_face_cascade():
	# Location of adaboost xml file for frontal face
	face_cascade_loc = os.path.join(
		haarcascades, "haarcascade_frontalface_alt.xml")
	face_cascade = cv.CascadeClassifier()
	if not face_cascade.load(cv.samples.findFile(face_cascade_loc)):
		print('--(!)Error loading face cascade')
		exit(0)
	
	return face_cascade

# Test function
if __name__ == "__main__":
	img = cv.imread("./Selfie_pic.jpeg")
	while True:
		exit_key = ord('q')

		# NOTE: waitKey returns an int, hence using bitwise AND
		if cv.waitKey(exit_key) & 255 == exit_key:
			cv.destroyAllWindows()
			break

		frame = face_detect(img, get_face_cascade())
		cv.namedWindow('img', cv.WINDOW_KEEPRATIO)
		cv.imshow('img', frame)