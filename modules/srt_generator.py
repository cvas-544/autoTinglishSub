import os

def format_timestamp(seconds: float) -> str:
    """
    Converts seconds to SRT timestamp format.
    Example: 1.5 → 00:00:01,500
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def generate_srt(chunks: list, output_path: str) -> str:
    """
    Takes word-level chunks from Whisper and generates .srt file.
    One word per subtitle block — popping effect ready.
    """

    srt_content = ""

    for i, chunk in enumerate(chunks):
        text = chunk["text"].strip()
        start, end = chunk["timestamp"]

        # Skip empty chunks
        if not text or start is None or end is None:
            continue

        srt_content += f"{i + 1}\n"
        srt_content += f"{format_timestamp(start)} --> {format_timestamp(end)}\n"
        srt_content += f"{text}\n\n"

    # Write to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    print(f"SRT saved to {output_path}")
    return output_path
