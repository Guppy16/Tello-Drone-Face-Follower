# %%
from djitellopy import Tello
from cv2 import cv2 as cv
import facedetect
from time import sleep

if __name__ == "__main__":
	tello = Tello()
	face_cascade = facedetect.get_face_cascade()

	try:
		tello.connect()
		tello.streamon()
		print(f"Battery: {tello.get_battery()}")

		frame = tello.get_frame_read()
		print("[INFO] dronecontrol.py - Got Frame Reader")

		while True:
			faces = facedetect.face_cascade_detect(frame.frame, face_cascade)
			detected_frame = facedetect.draw_face_box(frame.frame, faces)

			if detected_frame is None:
				raise ValueError("Error in dronecontrol.py - Frame not found")

			cv.imshow('frame', detected_frame)

			if cv.waitKey(1) & 0xFF == ord('q'):
				break

	except Exception as e:
		print("Error in dronecontrole.py")
		print(type(e))
		print(e)
		
	finally:
		cv.destroyAllWindows()
		tello.end()
# %%
