from process_image import process_image
from generate_narration import generate_narration
from create_video import create_video
from add_captions import add_subtitles
import os

def main():
    # Define file paths
    image_path = "assets/input.jpg"
    processed_image = "assets/processed.jpg"
    narration_audio = "assets/narration.mp3"
    background_music = "assets/music.mp3"
    output_video = "assets/output.mp4"
    caption_file = "assets/captions.srt"
    final_video = "assets/final_output.mp4"

    # Text content for overlay, narration, and subtitles
    text = "This is a sample video with text overlay"

    # Ensure assets folder exists
    os.makedirs("assets", exist_ok=True)

    print("Processing image...")
    process_image(image_path, processed_image, text)

    print("Generating narration...")
    generate_narration(text, narration_audio)

    print("Creating video with background music and narration...")
    create_video(processed_image, narration_audio, background_music, output_video)

    print("Generating captions...")
    with open(caption_file, "w") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:05,000\n")
        f.write(text + "\n\n")

    print("Adding subtitles...")
    add_subtitles(output_video, caption_file, final_video)

    print("Video generation complete! Check 'assets/final_output.mp4'.")

if __name__ == "__main__":
    main()
