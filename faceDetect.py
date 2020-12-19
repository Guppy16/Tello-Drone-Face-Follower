# %%
# NOTE: imported as such to disable linting errors due to C headers
from cv2 import cv2 as cv
# Location of cascades used for object detection
from cv2.data import haarcascades
import os
import numpy as np

# %%
def face_cascade_detect(frame, face_cascade):
	"""detect faces in a frame using face cascades. Returns a list of face positions"""

	if frame is None or np.shape(frame) == () or np.sum(frame) == 0:
		return

	frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	frame_gray = cv.equalizeHist(frame_gray)

	return face_cascade.detectMultiScale(frame_gray)


# %%
def draw_face_box(frame, faces):
	"""draw a bounding boxes around faces on a frame and number them"""

	if frame is None or np.shape(frame) == () or np.sum(frame) == 0:
		return

	for idx, (x, y, w, h) in enumerate(faces):
		frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
		frame = cv.putText(frame, f'{idx + 1}', (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255))

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
	face_cascade = get_face_cascade()

	while True:
		exit_key = ord('q')

		# NOTE: waitKey returns an int, hence using bitwise AND
		if cv.waitKey(exit_key) & 255 == exit_key:
			cv.destroyAllWindows()
			break

		faces = face_cascade_detect(img, face_cascade)
		frame = draw_face_box(img, faces)
		cv.namedWindow('img', cv.WINDOW_KEEPRATIO)
		cv.imshow('img', frame)