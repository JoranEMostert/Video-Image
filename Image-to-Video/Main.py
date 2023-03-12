import os
import cv2
import time
import moviepy.editor as mpe

# Create the output directory if it doesn't exist
if not os.path.exists('Video output'):
    os.makedirs('Video output')

# Check if output video file already exists
output_path = os.path.join('Video output', 'output.mp4')
if os.path.exists(output_path):
    # Append a timestamp to the output file name to avoid overwriting
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_path = os.path.join('Video output', f'output_{timestamp}.mp4')

# Search for any image file in the image input directory
image_files = [os.path.join('Image input', f) for f in os.listdir('Image input') if f.endswith('.jpg') or f.endswith('.jpeg')]

# Sort the image files in numerical order
image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Create a video writer object using moviepy library
fps = 24 # frames per second
video_clip = mpe.ImageSequenceClip(image_files, fps=fps)

# Search for any mp3 file in the audio input directory
audio_files = [f for f in os.listdir('Audio input') if f.endswith('.mp3')]
if len(audio_files) > 0:
    # Use the first mp3 file as the audio source
    audio_file = audio_files[0]
    # Create an audio clip object from the mp3 file
    audio_clip = mpe.AudioFileClip(os.path.join('Audio input', audio_file))
    # Check if video clip has an audio attribute before creating composite audio clip 
    if video_clip.audio:
        new_audio_clip = mpe.CompositeAudioClip([video_clip.audio, audio_clip])
    else:
        new_audio_clip = audio_clip 
    # Assign the composite audio clip to the video clip's audio attribute
    video_clip.audio = new_audio_clip

# Write the output video file with the added audio 
video_clip.write_videofile(output_path)

# Print a message when processing is complete
print("Done!")