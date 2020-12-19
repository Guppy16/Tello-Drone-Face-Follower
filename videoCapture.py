# %%
import numpy as np
from cv2 import cv2 as cv

# %%

def get_capture_stream(loc=0, frame_width: int=640, frame_height: int=480):
	"""Method to initialise input stream of video
	(from a camera connected to the device such as a webcam)"""
	cap = cv.VideoCapture(loc)
	cap.set(3, frame_width)    # Max val = 1280
	cap.set(4, frame_height)     # Max val = 720

	frame_width = int(cap.get(3))
	frame_height = int(cap.get(4))

	print(f"Frame width: {frame_width}, height: {frame_height}")

	return cap, frame_width, frame_height


def get_output_stream(loc: str="output.avi", enc: str='DIVX', frame_width: int=640, frame_height: int=480, fps=20):
	"""Method to initialise output stream of video"""
	fourcc = cv.VideoWriter_fourcc(*enc)
	out = cv.VideoWriter(loc, fourcc, fps, (frame_width, frame_height))

	return out

def release_streams(cap, out):
	cap.release()
	out.release()

if __name__ == "__main__":
	cap, frame_width, frame_height = get_capture_stream()
	out = get_output_stream()

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		out.write(frame)

		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
			
	cv.destroyAllWindows()
	release_streams(cap, out)

