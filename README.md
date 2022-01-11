# Tello Drone Face Follower

## Aims:

1. Face recognition
    - [x] In an image
    - [x] In a video stream from webcam
    - [x] In a Tello video stream
    - [ ] Only recognise face of "target"

2. Drone commands for basic flight control
    - [x] Get to grips with [djitellopy](https://github.com/damiafuentes/DJITelloPy)
    - [ ] Fly up and land down
    - [ ] Basic Maneuvers: fly up,down,left,right. rotate. Land

3. Face Follower
    - [ ] Average faces wrt position (maybe give more weighting to bigger faces?) AND wrt time (using exponential avg?)
    - [ ] Proportional control: very slowly translate up / down into frame and/or rotate into frame
    - [ ] Move closer to subject
    - [ ] PID controller for stable control

## ToDo:
- [ ] Requirement.txt (remove unnecessary dependencies)

---
## Useful stuff from other sources

- [DJI TelloPy](https://github.com/damiafuentes/DJITelloPy) Python API for Tello
- [hanyazou's implementation of TelloPy](https://github.com/hanyazou/TelloPy)

- [youngsol's implementation](https://github.com/youngsoul/tello-sandbox) required 3 threads
    i. operating the drone
    ii. recording video to mp4
    iii. displaying video stream
    
- [Selfie Air Stick](https://www.youtube.com/watch?v=RHRQoaqQIgo)
- [PyImageSearch Ball Tracking](https://github.com/Ubotica/telloCV/)
- [DJI Tello Drone Manual](https://dl-cdn.ryzerobotics.com/downloads/Tello/20180212/Tello+User+Manual+v1.0_EN_2.12.pdf)
- 



## NOTEs:
- Personal rating of the different face detection cascades tested in video stream:
    - haarcascade_frontalface_alt: 
    - haarcascade_frontalface_alt_tree: Pretty good. Detects my neck as a face
    - haarcascade_frontalface_alt2: Pretty good. Detects my neck as a face
    - haarcascade_frontalface_default: Doesn't work that well
