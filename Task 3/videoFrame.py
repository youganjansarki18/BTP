import os
import cv2

frame_folder = "C:\\Users\\youga\\Desktop\\BTP\\Task 2\\code_02\\output"
output_video_path = "output_video_30.mp4"

# Get the list of PNG frames
frame_files = [f for f in os.listdir(frame_folder) if f.endswith(".png")]
frame_files.sort()  # Ensure frames are in order

# Read the first frame to get dimensions
first_frame = cv2.imread(os.path.join(frame_folder, frame_files[0]))
height, width, layers = first_frame.shape

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # You can change the codec as needed
out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))

# Iterate through frames and write to video
for frame_filename in frame_files:
    frame_path = os.path.join(frame_folder, frame_filename)
    frame = cv2.imread(frame_path)
    out.write(frame)

# Release video writer and close the video file
out.release()

print("Video creation completed.")