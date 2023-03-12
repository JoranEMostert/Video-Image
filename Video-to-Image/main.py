import cv2
import os
import time

# Define a loading animation
def loading_animation():
    animation = "|/-\\"
    for i in range(30):
        time.sleep(0.1)
        print(f"\rConverting video files {animation[i % len(animation)]}", end="", flush=True)

# Create the output directory if it doesn't exist
if not os.path.exists('Image output'):
    os.makedirs('Image output')

# Search for any video file in the video input directory
video_files = [f for f in os.listdir('video input') if f.endswith('.mp4') or f.endswith('.avi')]

# Loop through each video file and convert it to images
for video_file in video_files:
    # Remove any numbers from the video file name
    video_name = ''.join(filter(lambda x: not x.isdigit(), video_file))

    # Open the video file
    cap = cv2.VideoCapture(os.path.join('video input', video_file))

    # Create a counter for the images
    count = 0

    # Loop through the frames in the video
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        # If there are no more frames, break out of the loop
        if not ret:
            break

        # Save the frame as an image in the output directory
        cv2.imwrite(os.path.join('Image output', f'{video_name}_{count}.jpg'), frame)

        # Increment the counter
        count += 1

    # Release the video file
    cap.release()

    # Show the loading animation
    loading_animation()

print("\rDone!") # Print "Done!" once all video files are converted