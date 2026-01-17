import streamlit as st
import subprocess
import whisper
from transformers import pipeline
from moviepy.editor import VideoFileClip
import os

# Create folders
os.makedirs("uploads", exist_ok=True)
os.makedirs("clips", exist_ok=True)

st.title("🎬 PulsePoint AI - Reel Generator")
st.write("Upload a long video or paste a YouTube link to generate short reels automatically!")

# Whisper + Sentiment models
model = whisper.load_model("small")
sentiment = pipeline("sentiment-analysis")

def download_youtube(url):
    st.info("⏳ Downloading YouTube video... Please wait.")

    # Clean URL (remove playlist, timestamp)
    if "&" in url:
        url = url.split("&")[0]

    output_path = "uploads/video.mp4"

    cmd = [
        "yt-dlp",
        "--no-playlist",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "--merge-output-format", "mp4",
        "-o", output_path,
        url
    ]

    with st.spinner("📥 Downloading and merging video streams..."):
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if process.returncode != 0:
        st.error("❌ Failed to download video. Check the link and try again.")
        st.code(process.stderr)
        return None

    st.success("✅ Video downloaded successfully!")
    return output_path


video_path = None

# ==== INPUT SECTION ====
yt_link = st.text_input("Paste YouTube Link (optional)")

uploaded_file = st.file_uploader("Upload Video (MP4/MOV)", type=["mp4", "mov"])

if yt_link:
    video_path = download_youtube(yt_link)

elif uploaded_file:
    video_path = f"uploads/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

# ==== PROCESS BUTTON ====
if video_path and st.button("Generate Reels 🎯"):

    st.success("Video loaded! Extracting transcript...")
    
    result = model.transcribe(video_path)
    segments = result["segments"]

    st.subheader("📝 Transcript Preview:")
    st.write(result["text"][:1000] + "...")

    # Sentiment Analysis
    emotional_scores = []
    for seg in segments:
        score = sentiment(seg["text"])[0]
        emotional_scores.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"],
            "label": score["label"],
            "confidence": score["score"]
        })

    # Pick Top Segments
    emotional_scores = sorted(emotional_scores, key=lambda x: x["confidence"], reverse=True)
    top_segments = emotional_scores[:5]

    st.subheader("🔥 Top Emotional Moments Chosen:")
    for ts in top_segments:
        st.write(f"➡ `{ts['label']} ({ts['confidence']:.2f})` | {ts['text']}")

    # Generate Clips
    st.info("Cutting video clips...")
    video = VideoFileClip(video_path)
    clip_paths = []

    for i, seg in enumerate(top_segments):
        clip = video.subclip(seg["start"], seg["end"])
        clip_path = f"clips/reel_{i+1}.mp4"
        clip.write_videofile(clip_path, codec="libx264", audio_codec="aac", verbose=False)
        clip_paths.append(clip_path)

    st.success("✅ Reels Generated!")

    # Show & Download
    for i, cp in enumerate(clip_paths, start=1):
        st.video(cp)
        with open(cp, "rb") as f:
            st.download_button(
                label=f"Download Reel {i}",
                data=f.read(),
                file_name=f"reel_{i}.mp4",
                mime="video/mp4"
            )
