# %%
from cv2 import cv2 as cv
from faceDetect import face_detect, get_face_cascade
from videoCapture import getCaptureStream, getOutputStream, releaseStreams

# main function to get video feed from webcam and detect a face

def main_loop(cap, out, face_cascade):
	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		out.write(frame)

		frame = face_detect(frame, face_cascade=face_cascade)
		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

if __name__ == "__main__":
	face_cascade = get_face_cascade()

	cap, frame_width, frame_height = getCaptureStream()
	out = getOutputStream()

	try:
		main_loop(cap, out, face_cascade)
	except Exception as e:
		print(f"Error in main loop")
		print(e)
	finally:
		# Release windows and streams
		cv.destroyAllWindows()
		releaseStreams(cap, out)