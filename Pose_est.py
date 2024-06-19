import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    # Read image from file
    frame = cv2.imread(r"C:\Users\\OneDrive\Desktop\VS_CODES\raise hand3.jpg")

    # Recolor image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Make detection
    results = pose.process(image)

    # Recolor back to BGR
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Define the names of the landmarks
    landmark_names = {
        11: "Left shoulder",
        12: "Right shoulder",
        13: "Left elbow",
        14: "Right elbow",
        15: "Left wrist",
        16: "Right wrist",
        
    }

    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark
        # Upper body points are from 11 to 16 and 23 to 28
        upper_body_landmarks = landmarks[11:16]

        # Create a dictionary to store coordinates
        coordinates = {}

        # Print and write each landmark's name and coordinates
        with open(r"C:\Users\\OneDrive\Desktop\VS_CODES\output.txt", "w") as outfile:
            for i, landmark in enumerate(upper_body_landmarks):
                coordinates[landmark_names[i + 11]] = (landmark.x, landmark.y, landmark.z)
                outfile.write(f"{landmark_names[i + 11]}: x={landmark.x}, y={landmark.y}, z={landmark.z}\n")

        # Access coordinates as needed, for example:
        # left_shoulder_x, left_shoulder_y, left_shoulder_z = coordinates["Left shoulder"]

    except:
        pass

    # Render detections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                              )

    cv2.imshow('Mediapipe Feed', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
