# Robotics Project: Humanoid Robot Pose Mimicry

## Overview
This project involves capturing and processing human upper body pose information using the Mediapipe library and transmitting the relevant joint angles to a humanoid robot (NAO) using the NAOqi framework. The goal is to enable the robot to mimic the detected upper body pose of a human.

## Components
1. **Human Pose Detection:**
   - Uses the Mediapipe library to detect and extract key landmarks of the upper body from an input image.
   - Landmark coordinates are stored in a text file for further use.

2. **Robot Motion Control:**
   - Uses the NAOqi framework to control the motion of a humanoid robot based on the extracted pose information.
   - Joint angles are read from the text file and interpolated to mimic the detected upper body pose.

## Requirements
- OpenCV
- Mediapipe
- NAOqi (Python SDK for controlling NAO humanoid robots)

## Setup
1. Ensure all required libraries are installed (`cv2`, `mediapipe`, and `naoqi`).
2. Run the pose detection component to capture and store upper body pose information.
3. Run the robot motion control component to make the humanoid robot mimic the detected upper body pose.

## Documentation
For detailed documentation, including the Denavit-Hartenberg (DH) model of the NAO robot, please refer to ahmedemadtawfik@gmail.com

## Usage
1. Adjust file paths and IP addresses in the code according to your setup.
2. Fine-tune time durations in the robot motion code for smoother movements.

## Contribution
Feel free to contribute by opening issues or creating pull requests. Your feedback and enhancements are welcome!
---


