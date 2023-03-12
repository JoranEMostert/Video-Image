# Video-Image

This project contains two programs that can be used to convert video to image files and vice versa. 

## Programs

1. `video_to_image.py`: This program can be used to convert an MP4 video file into a series of JPEG image files. Each frame of the video is saved as a separate image file. 
2. `image_to_video.py`: This program can be used to convert a series of JPEG image files back into an MP4 video file. The program also allows the user to add their own MP3 audio file to the new MP4 video that will be generated.

## Usage

To use these programs, simply put the required files in the correct directory and run the `run.bat` file. The settings for the programs can be adjusted in the `main.py` file. Please note that some knowledge of coding is required to modify the settings in the `main.py` file.

## Requirements

This project requires Python to be installed on your computer. Additionally, the dependencies required for this project can be installed by running the `Dependencies.bat` file.

## Background

I created this project because I wanted to make stable diffusion videos, which were not yet available at the time. To accomplish this, I used image to image batch functionality. 

## Examples

***input***

<video controls>
  <source src="/Video-to-Image/video input/jujutsu.mp4" type="video/mp4">
</video>

***input***

<video controls>
  <source src="/Image-to-Video/Video output/output_20230312-215659.mp4" type="video/mp4">
</video>

## Credits

This project was created by Joran Mostert.
