# Exercise 95 — Convert a MP4 video to MP3 audio
# Requires: moviepy (pip install moviepy)
# ─────────────────────────────────────────────────────────────────────────────

import os

def convert_mp4_to_mp3(input_path: str, output_path: str = None):
    try:
        from moviepy.editor import VideoFileClip
        if not os.path.isfile(input_path):
            print(f"File not found: {input_path}")
            return
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + ".mp3"
        clip = VideoFileClip(input_path)
        clip.audio.write_audiofile(output_path)
        clip.close()
        print(f"Converted: {output_path}")
    except ImportError:
        print("moviepy not installed. Run: pip install moviepy")

def main():
    input_path = input("Enter the path to the MP4 file: ").strip()
    convert_mp4_to_mp3(input_path)

if __name__ == "__main__":
    main()
