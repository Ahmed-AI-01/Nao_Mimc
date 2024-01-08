from naoqi import ALProxy

# Replace "IP" and "PORT" with your robot's IP address and port
motion = ALProxy("ALMotion", "10.1.95.107", 9559)
posture_service = ALProxy("ALRobotPosture", "10.1.95.107", 9559)

# Define joint names and corresponding angles
joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
               "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]

# Read joint coordinates from the text file
with open(r"C:\Users\PrideGod\OneDrive\Desktop\VS_CODES\output.txt", "r") as infile:
    lines = infile.readlines()

# Extract joint angles from the file
joint_angles = []
for line in lines:
    # Extract the numerical values from each line
    values = [float(val.split("=")[1]) for val in line.strip().split(", ")]
    joint_angles.extend(values)

# Set the time for each motion to take in seconds
time_lists = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]  # Adjust these times as needed

# Set the motion to be absolute
is_absolute = True

# Make the robot go to the posture named "Stand"
posture_service.goToPosture("Stand", 0.5)
# Execute the motion interpolation

motion.angleInterpolation(joint_names, joint_angles, time_lists, is_absolute)