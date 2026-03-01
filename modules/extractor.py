import subprocess
import os

def extract_audio(video_path: str, output_dir: str) -> str:
    """
    Extracts audio from video file using FFmpeg.
    Returns path to extracted .wav file.
    """
    
    # Get filename without extension
    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{filename}.wav")

    command = [
        "ffmpeg",
        "-i", video_path,       # input video
        "-ar", "16000",         # 16kHz sample rate (Whisper needs this)
        "-ac", "1",             # mono audio (Whisper needs this)
        "-y",                   # overwrite if exists
        output_path
    ]

    print(f"Extracting audio from {video_path}...")
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Audio saved to {output_path}")

    return output_path