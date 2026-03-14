# autoTinglishSub — Project Rules & Context

## What It Does
Local CLI: video → FFmpeg extract audio → Whisper transcribe → word-level `.srt` for CapCut/VN pop animations.
Optimised for Telugu + Indian English (Tinglish) code-switching.

---

## Model
- HF: `cvas-544/autotinglishsub-whisper-telugu`
- Lineage: `vasista22/whisper-telugu-large-v2` → fine-tuned on 105 Tinglish audio chunks, 10 epochs, RTX 3090
- WER: 75% → 15.1%
- `alignment_heads` hardcoded in `transcriber.py` for word-level timestamps

---

## Project Structure
```
AutoSub/
├── main.py                   ← CLI entry point (-i input -o output)
├── modules/
│   ├── extractor.py          ← FFmpeg audio extract
│   ├── transcriber.py        ← Whisper inference (transformers pipeline)
│   └── srt_generator.py      ← word-level .srt writer
├── training.py               ← Fine-tuning script (Seq2SeqTrainer)
├── requirements.txt          ← CPU inference deps
├── train-requirements.txt    ← GPU training deps (install on RunPod)
├── GPU-requirements.txt      ← RunPod base env (torch 2.4.1+cu124, NO training packages)
├── input/                    ← drop videos here
└── output/                   ← .srt files saved here
```

---

## Inference Usage
```bash
python main.py -i input/video.mp4
```
Model auto-downloads from HF on first run.

---

## CT2 Conversion — Done ✅
- Converted with `ct2-transformers-converter --quantization int8`
- Local output: `autotinglishsub-ct2/` (model.bin ~1.56GB)
- Pushed to HF: `cvas-544/autotinglishsub-whisper-telugu-ct2`
- `transcriber.py` updated to use `faster-whisper` (WhisperModel)
- `requirements.txt` updated: removed torch/transformers, added faster-whisper
- transformers upgraded to 5.3.0 in venv (required by ctranslate2 4.7.1)

---

## RunPod Settings (for next session)
| Setting | Value |
|---|---|
| Pod name | autoTinglishSub |
| GPU | RTX 3090 × 1 |
| vCPU | 32 |
| Memory | 125 GB |
| Container disk | 40 GB |
| Volume (workspace) | 80 GB @ `/workspace` |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-...` |
| Template | `runpod-torch-v240` |
| Location | EU-CZ-1 (Secure cloud) |
| Cost | ~$0.48/hr ($0.46 compute + storage) |

---

## Future Fine-Tuning (RunPod)
1. Spin up RunPod PyTorch image (torch+CUDA pre-installed)
2. `pip install -r train-requirements.txt`
3. Run `training.py` — key args: `--model_name`, `--train_datasets`, `--eval_datasets`, `--language Telugu`
4. Key settings: `save_total_limit=10`, `eval_strategy`, `processing_class` (NOT `tokenizer`)
5. `optim="adamw_bnb_8bit"` requires bitsandbytes

---

## Current State
- ✅ Model live on HuggingFace (`cvas-544/autotinglishsub-whisper-telugu`)
- ✅ CT2 model live on HuggingFace (`cvas-544/autotinglishsub-whisper-telugu-ct2`)
- ✅ `transcriber.py` uses `faster-whisper` (4-5x faster CPU inference)
- ✅ `training.py` synced with pod patched script
- ✅ `train-requirements.txt` created
- ✅ `app.py` — Gradio UI built (split panel: Input left, Output right, Generate button full-width)
- 🔜 Fine-tune model further before deploying UI
- 🔜 Deploy `app.py` to HuggingFace Spaces after fine-tuning
