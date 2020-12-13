# %%
import numpy as np
from cv2 import cv2 as cv

# %%

def getCaptureStream(loc=0, frame_width: int=640, frame_height: int=480):
	"""Method to initialise input stream of video"""
	cap = cv.VideoCapture(loc)
	cap.set(3, frame_width)    # Max val = 1280
	cap.set(4, frame_height)     # Max val = 720

	frame_width = int(cap.get(3))
	frame_height = int(cap.get(4))

	print(f"Frame width: {frame_width}, height: {frame_height}")

	return cap, frame_width, frame_height


def getOutputStream(loc: str="output.avi", enc: str='DIVX', frame_width: int=640, frame_height: int=480, fps=20):
	"""Method to initialise output stream of video"""
	fourcc = cv.VideoWriter_fourcc(*enc)
	out = cv.VideoWriter(loc, fourcc, fps, (frame_width, frame_height))

	return out

def releaseStreams(cap, out):
	cap.release()
	out.release()

if __name__ == "__main__":
	cap, frame_width, frame_height = getCaptureStream()
	out = getOutputStream()

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		out.write(frame)

		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
			
	cv.destroyAllWindows()
	releaseStreams(cap, out)

