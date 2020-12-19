# %%
from cv2 import cv2 as cv
import facedetect
from videocapture import get_capture_stream, get_output_stream, release_streams

# main function to get video feed from webcam and detect a face

def main_loop(cap, out, face_cascade):
	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		out.write(frame)

		faces = facedetect.face_cascade_detect(frame, face_cascade)
		frame = facedetect.draw_face_box(frame, faces)
		cv.imshow('frame', frame)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break

if __name__ == "__main__":
	face_cascade = facedetect.get_face_cascade()

	cap, frame_width, frame_height = get_capture_stream()
	out = get_output_stream()

	try:
		main_loop(cap, out, face_cascade)
	except Exception as e:
		print(f"Error in main loop")
		print(e)
	finally:
		# Release windows and streams
		cv.destroyAllWindows()
		release_streams(cap, out)