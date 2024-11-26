from PIL import Image
import cv2
import os
from glob import glob

# Root folder containing all video folders
root_folder = "train_data/"

# Iterate through all video folders in the root directory
video_folders = sorted(glob(os.path.join(root_folder, "video*")))

for video_folder in video_folders:
    video_path = os.path.join(video_folder, "video_left.avi")
    output_folder = os.path.join(video_folder, "frames") 
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(video_path):
        print(f"Video not found: {video_path}")
        continue

    print(f"Processing: {video_path}")

    # Open video and extract properties
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))  
    interval = fps // 1  

    frame_id = 0
    saved_frame_id = 0

    while True:
        ret, frame = video.read()
        if not ret:  
            break

        if frame_id % interval == 0:
            frame_name = os.path.join(output_folder, f"{frame_id:09d}.png")
            cv2.imwrite(frame_name, frame)  
            saved_frame_id += 1

        frame_id += 1

    video.release()

print("All videos processed.")
