Image to Video Generator

This Python project takes an image, overlays text, applies transformations, and converts it into a short video with background music, captions, and narration.

Features

Converts an image into a video with background music.

Overlays text onto the image.

Applies grayscale transformation.

Generates a voiceover from the text using gTTS.

Adds captions (subtitles) to the video.

Uses FFmpeg for video creation and processing.

Installation

1. Clone the Repository

git clone https://github.com/your-repo/image_to_video_project.git
cd image_to_video_project

2. Install Dependencies

Run the following command to install required libraries:

pip install pillow gtts moviepy numpy ffmpeg-python

3. Install FFmpeg

Ensure FFmpeg is installed on your system:

ffmpeg -version

If FFmpeg is not installed:

Windows: Download and install from FFmpeg official site.

Mac: Install via Homebrew: brew install ffmpeg.

Linux: Install using APT: sudo apt install ffmpeg.

Usage

1. Place Your Files in assets/

Before running the script, ensure you have:

An input image (input.jpg) in assets/.

A background music file (music.mp3) in assets/.

2. Run the Program

Navigate to the src/ directory and execute:

python src/main.py

3. Output Files

After execution, the following files will be generated in assets/:

processed.jpg → Processed image with text overlay.

narration.mp3 → Audio narration generated from text.

output.mp4 → Video with background music and narration.

captions.srt → Subtitle file.

final_output.mp4 → Final video with captions.

4. View the Final Video

Open assets/final_output.mp4 to watch your video.

Contact

For questions or feedback, reach out via email @jeremyajoku11@gmail.com