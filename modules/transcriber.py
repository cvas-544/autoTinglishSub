from faster_whisper import WhisperModel

def transcribe_audio(audio_path: str) -> list:
    """
    Transcribes using faster-whisper — memory efficient.
    """

    print("Loading model...")
    model = WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8"      # compressed — uses way less RAM
    )

    print(f"Transcribing {audio_path}...")
    segments, info = model.transcribe(
        audio_path,
        language="te",
        word_timestamps=True,
        initial_prompt="నమస్కారం. This video is in Telugu and English mixed."
    )

    chunks = []
    for segment in segments:
        for word in segment.words:
            chunks.append({
                "text": word.word,
                "timestamp": (word.start, word.end)
            })

    return chunks