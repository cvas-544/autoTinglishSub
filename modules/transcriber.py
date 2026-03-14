from faster_whisper import WhisperModel

def transcribe_audio(audio_path: str) -> list:
    print("Loading fine-tuned model (faster-whisper / CTranslate2)...")

    model = WhisperModel(
        "cvas-544/autotinglishsub-whisper-telugu-ct2",
        device="cpu",
        compute_type="int8"
    )

    print(f"\nTranscribing {audio_path}...")

    segments, info = model.transcribe(
        audio_path,
        language="te",
        word_timestamps=True,
        beam_size=5
    )

    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})")

    chunks_out = []
    for segment in segments:
        for word in segment.words:
            chunks_out.append({
                "text": word.word,
                "timestamp": (round(word.start, 3), round(word.end, 3))
            })

    print(f"\n✅ Transcription complete! {len(chunks_out)} words found.")
    return chunks_out
