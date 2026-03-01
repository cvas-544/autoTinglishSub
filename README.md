# autoTinglishSub 🎬

A local-first CLI tool for generating word-level subtitles 
for Telugu and Indian English short-form videos.

## Installation

1. Clone the repo and 
cd autoTinglishsub

2. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Install FFmpeg:

# Mac
brew install ffmpeg

# Ubuntu/Linux
sudo apt install ffmpeg

# Windows
winget install ffmpeg

## Usage

python main.py -i input/video.mp4

## Output
Word-level .srt file saved to output/ folder.
Ready for CapCut, VN, Premiere Pro.

## Roadmap
- [ ] Fine-tuned Telugu + Indian English model
- [ ] Code-switching support
- [ ] HuggingFace model publish
