# Tello Drone Face Follower

## Aims:

1. Face recognition
    - [x] In an image
    - [ ] In a video
    - [ ] In a Tello video stream

2. Drone commands for basic flight control
    - [ ] Use some Tello Python API
    - [ ] Fly up and land down
    - [ ] Basic Maneuvers: fly up,down,left,right. rotate. Land

3. Face Follower
    - [ ] Proportional control: very slowly translate up / down into frame and/or rotate into frame
    - [ ] Move closer to subject
    - [ ] PID controller for stable control

---
## Useful stuff from other sources

- [DJI TelloPy](https://github.com/damiafuentes/DJITelloPy) Python API for Tello

- [youngsol's implementation](https://github.com/youngsoul/tello-sandbox) required 3 threads
    i. operating the drone
    ii. recording video to mp4
    iii. displaying video stream