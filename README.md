# autoTinglishSub 🎬

Local-first CLI tool for generating **word-level "popping" subtitles** for Telugu and Indian English short-form videos.

Powered by a custom fine-tuned Tinglish Whisper model:

👉 Hugging Face Model:  
https://huggingface.co/cvas-544/autotinglishsub-whisper-telugu  

---

## 🚀 What This Tool Does

autoTinglishSub:

- Extracts audio from video using FFmpeg  
- Transcribes using a fine-tuned Whisper model  
- Generates strict word-level timestamps  
- Outputs single-word segmented `.srt` files  
- Enables high-retention animated subtitles in CapCut, VN, and Premiere Pro  

Built for creators working with:

- Telugu conversational speech  
- Indian English accents  
- Telugu + English code-switching  
- Fast-paced reel-style delivery  

---

## 🧠 Model

This CLI integrates:

**cvas-544/autotinglishsub-whisper-telugu**

Model Lineage:
- Fine-tuned from `vasista22/whisper-telugu-large-v2` (Apache 2.0)
- Originally based on `openai/whisper-large-v2` (MIT)

Optimized specifically for Tinglish subtitle workflows.

---

## ✨ Features

- Word-level subtitle segmentation  
- `.srt` export  
- Optimized for Telugu + Indian English  
- Local execution (no cloud dependency)  
- Creator-focused subtitle formatting  

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/autoTinglishSub.git
cd autoTinglishSub
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

**Mac:**
```bash
brew install ffmpeg
```

**Ubuntu/Linux:**
```bash
sudo apt install ffmpeg
```

**Windows:**
```bash
winget install ffmpeg
```

---

## 🚀 Usage

```bash
python main.py -i input/video.mp4
```

---

## 📤 Output

- Word-level .srt file
- Saved to output/ directory
- Ready to import into:
  - CapCut
  - VN Editor
  - Adobe Premiere Pro

Apply "Pop" or "Spring" animation to the text track for the signature effect.

---

## 🎯 Intended Use

Designed for:

- Reels
- YouTube Shorts
- Instagram content
- Podcast clips
- Tech explainers
- Motivational edits

---

## 🔮 Roadmap

- Automatic model download from Hugging Face
- Code-switching accuracy improvements
- Word-level timing refinement
- Beat-synced subtitle mode
- GUI wrapper
- Direct CapCut XML export

---

## 📄 License

This project uses a model licensed under Apache 2.0.
See the model card for details:
https://huggingface.co/cvas-544/autotinglishsub-whisper-telugu

---

## 👨‍💼 Author

Built by Vasu Chukka

📬 vasu.chukka@outlook.com  
💻 https://www.linkedin.com/in/vasu-chukka-1a3569116/