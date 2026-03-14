import gradio as gr
import os
import tempfile
from modules.extractor import extract_audio
from modules.transcriber import transcribe_audio
from modules.srt_generator import generate_srt


def process_video(video_path):
    if video_path is None:
        return None, "No video uploaded.", ""

    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = extract_audio(video_path, tmpdir)
        chunks = transcribe_audio(audio_path)

        filename = os.path.splitext(os.path.basename(video_path))[0]
        srt_path = os.path.join(tmpdir, f"{filename}.srt")
        generate_srt(chunks, srt_path)

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        final_srt = os.path.join(output_dir, f"{filename}.srt")
        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()
        with open(final_srt, "w", encoding="utf-8") as f:
            f.write(srt_content)

        words = [chunk["text"].strip() for chunk in chunks if chunk["text"].strip()]
        preview = " ".join(words)

        return final_srt, f"✅ Done — {len(words)} words transcribed.", preview


css = """
#title { text-align: center; font-size: 2rem; font-weight: 700; margin-bottom: 0.2rem; }
#subtitle { text-align: center; color: #888; margin-bottom: 1.5rem; }
#generate-btn { font-size: 1rem; }
#preview-box textarea { font-family: monospace; font-size: 0.95rem; line-height: 1.8; }
.panel-label { font-size: 0.75rem; font-weight: 600; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
"""

with gr.Blocks(css=css, title="autoTinglishSub") as demo:

    gr.Markdown("# autoTinglishSub", elem_id="title")
    gr.Markdown("Word-level subtitles for Telugu & Tinglish videos", elem_id="subtitle")

    generate_btn = gr.Button("Generate Subtitles", elem_id="generate-btn", size="lg")

    with gr.Row(equal_height=True):

        # Left — Input
        with gr.Column():
            gr.Markdown("**INPUT**", elem_classes="panel-label")
            video_input = gr.Video(label="Upload Video")
            status_box = gr.Textbox(
                label="Status",
                interactive=False,
                placeholder="Upload a video and click Generate..."
            )

        # Right — Output
        with gr.Column():
            gr.Markdown("**OUTPUT**", elem_classes="panel-label")
            preview_box = gr.Textbox(
                label="Transcript",
                interactive=False,
                lines=16,
                placeholder="Transcript will appear here...",
                elem_id="preview-box"
            )
            srt_output = gr.File(label="Download .srt")

    generate_btn.click(
        fn=process_video,
        inputs=[video_input],
        outputs=[srt_output, status_box, preview_box]
    )


if __name__ == "__main__":
    demo.launch()
