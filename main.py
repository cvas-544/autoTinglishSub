import argparse
import os
from modules.extractor import extract_audio
from modules.transcriber import transcribe_audio
from modules.srt_generator import generate_srt

def main():
    parser = argparse.ArgumentParser(
        description="AutoSub — Telugu & Indian English subtitle generator"
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to input video file"
    )

    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Directory to save SRT file (default: output/)"
    )

    args = parser.parse_args()

    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: File not found — {args.input}")
        return

    # Create output dir if not exists
    os.makedirs(args.output, exist_ok=True)

    # Get output SRT path
    filename = os.path.splitext(os.path.basename(args.input))[0]
    srt_path = os.path.join(args.output, f"{filename}.srt")

    # Pipeline
    print("\n--- AutoSub Starting ---\n")
    audio_path = extract_audio(args.input, args.output)
    chunks = transcribe_audio(audio_path)
    generate_srt(chunks, srt_path)

    print(f"\n--- Done! SRT saved to {srt_path} ---\n")

if __name__ == "__main__":
    main()