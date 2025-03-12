'''
create video with music
'''

import subprocess

def create_video(image_path, audio_path, music_path, output_video, duration=5):
    """
    Generates a video from a static image, mixes background music and narration.

    :param image_path: Path to the image.
    :param audio_path: Path to narration audio file.
    :param music_path: Path to background music.
    :param output_video: Path to save the final video.
    :param duration: Duration of the video in seconds (default: 5 seconds).
    """
    try:
        # Create a video from the image with audio mixing
        video_cmd = [
            "ffmpeg", "-y",
            "-loop", "1",  # Loop image for the entire video
            "-i", image_path,  # Input image
            "-i", music_path,  # Background music
            "-i", audio_path,  # Narration
            "-c:v", "libx264", "-t", str(duration), "-pix_fmt", "yuv420p",
            "-filter_complex", "[1:a][2:a]amix=inputs=2:duration=first:dropout_transition=3[aout]",  # Mix audio tracks
            "-map", "0:v", "-map", "[aout]",  # Map video and audio
            output_video
        ]

        subprocess.run(video_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Video created: {output_video}")
    
    except Exception as e:
        print(f"Error creating video: {e}")
