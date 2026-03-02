import torch
from transformers import pipeline

def transcribe_audio(audio_path: str) -> list:
    print("Loading fine-tuned model...")
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    
    transcriber = pipeline(
        task="automatic-speech-recognition",
        model="cvas-544/autotinglishsub-whisper-telugu",
        chunk_length_s=30,
        device=device
    )

    print(f"Transcribing {audio_path}...")
    result = transcriber(audio_path, return_timestamps="word")

    chunks = []
    for chunk in result["chunks"]:
        chunks.append({
            "text": chunk["text"],
            "timestamp": (
                round(chunk["timestamp"][0], 3),
                round(chunk["timestamp"][1], 3)
            )
        })

    return chunks
