'''
add captions to the video
'''

import subprocess

def add_subtitles(video_input, subtitle_file, video_output):
    """
    Adds subtitles to a video using FFmpeg.

    :param video_input: Path to the input video.
    :param subtitle_file: Path to the subtitle (.srt) file.
    :param video_output: Path to save the final video with subtitles.
    """
    try:
        subtitle_cmd = [
            "ffmpeg", "-y",
            "-i", video_input,
            "-vf", f"subtitles={subtitle_file}:force_style='Fontsize=24,PrimaryColour=&H00FFFFFF'",
            "-c:a", "copy",
            video_output
        ]

        subprocess.run(subtitle_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Subtitled video saved at {video_output}")

    except Exception as e:
        print(f"Error adding subtitles: {e}")
