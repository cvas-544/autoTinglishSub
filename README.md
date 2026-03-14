# autoTinglishSub 🎬

Local-first CLI tool for generating **word-level "popping" subtitles** for Telugu and Indian English short-form videos.

Powered by a custom fine-tuned Tinglish Whisper model: 
👉 Hugging Face Model (original):
https://huggingface.co/cvas-544/autotinglishsub-whisper-telugu

converted to CTranslate2 for 4-5x faster CPU inference:
👉 Hugging Face Model (CT2 / faster-whisper):
https://huggingface.co/cvas-544/autotinglishsub-whisper-telugu-ct2

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

**cvas-544/autotinglishsub-whisper-telugu-ct2** (active — faster-whisper / CTranslate2)

Model Lineage:
- Base: `openai/whisper-large-v2` (MIT)
- Telugu checkpoint: `vasista22/whisper-telugu-large-v2` (Apache 2.0)
- Fine-tuned → `cvas-544/autotinglishsub-whisper-telugu` (Round 1)
- Converted → `cvas-544/autotinglishsub-whisper-telugu-ct2` (int8 quantization)

Training Results (Round 1):
- WER reduced from 75% → 15.1%
- Trained on 105 Telugu+English creator-style audio chunks
- 10 epochs on RTX 3090

CT2 Conversion:
- Converted with `ct2-transformers-converter --quantization int8`
- Model size reduced from ~3GB to ~1.56GB
- 4-5x faster CPU inference via `faster-whisper`
- No GPU required for inference

---

## ✨ Features

- Word-level subtitle segmentation  
- `.srt` export  
- Optimized for Telugu + Indian English  
- Local execution (no cloud dependency)
- Transcribes using cvas-544/autotinglishsub-whisper-telugu (auto-downloaded)  
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

- Automatic model download from Hugging Face — ✅ Done
- CT2 conversion + int8 quantization — ✅ Done
- Round 1 fine-tuning (Telugu + Tinglish, WER 75% → 15.1%) — ✅ Done
- Round 2 fine-tuning (more Tinglish data, accent variety) — 🔜 Pending
- Gradio web UI — 🔜 In progress
- Deploy to Hugging Face Spaces — 🔜 Pending (after Round 2 fine-tuning)
- Support for additional Indian languages (Tamil, Kannada, Hindi) — 🔜 Future
- Word-level timing refinement
- Beat-synced subtitle mode
- Direct CapCut XML export

---

## 🤝 Contributing

Looking for collaborators to extend language support for Indian content creators.

If you work with Tamil, Kannada, Hindi, Malayalam, or other Indian language audio data — I'd love to connect and expand this beyond Telugu.

Open an issue or reach out directly.

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
