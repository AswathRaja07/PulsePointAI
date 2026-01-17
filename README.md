# 🎬 PulsePoint AI — Reel Generator

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JQXUgloZvpcNWOjkNV_DJDT2Noxms85S?usp=sharing)

**By:** Aswath Raja R  
**Tagline:** AI tool that converts long videos into short reels using emotional peaks.

---

## � Overview

Mentors, educators, and creators produce hours of long-form content (lectures, workshops, podcasts).  
Modern viewers consume content in 30–60 second bursts.

**PulsePoint AI** solves this by automatically converting long videos into short reels using:

- Emotional peak detection
- Speech-to-text transcription
- Sentiment analysis
- Automatic video clipping

This makes education **snackable, shareable, and engagement-friendly**.

---

## ✨ Features

- Upload video OR paste YouTube link
- Whisper transcription (accurate speech-to-text)
- Emotional peak detection from transcript
- Sentiment scoring (Positive / Negative / Neutral)
- Automatic reel selection (top 3–5 clips)
- Fast video clipping via FFmpeg (no re-encode)
- Watch & download generated reels
- Clean Web UI (Streamlit)

---

## 🧠 How It Works

PulsePoint AI identifies "interesting" parts of video by combining:

1. **Speech-to-Text** — Whisper extracts transcript with timestamps
2. **Sentiment Analysis** — HuggingFace Transformers detect emotional intensity
3. **Peak Selection** — Top emotional segments chosen by confidence score
4. **Clip Extraction** — FFmpeg cuts reels instantly with stream copy

---

## 🛠 Tech Stack

### Backend / Processing
| Component | Tool |
|---|---|
| Speech-to-text | OpenAI Whisper |
| Sentiment analysis | HuggingFace Transformers |
| Video clipping | FFmpeg |
| Video download | yt-dlp |
| Model runtime | PyTorch |
| GPU Support | CUDA (Colab) |

### Frontend / UI
| Component | Tool |
|---|---|
| Web Framework | Streamlit |
| Reverse Tunnel | Ngrok |

---

## 📂 Project Structure

```
PulsePointAI/
├── app.py
├── README.md
├── requirements.txt
├── uploads/        # input video
└── clips/          # generated reels
```

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/PulsePointAI.git
   cd PulsePointAI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥 Usage

1. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

2. **Use the UI:**
   - Upload a video **or**
   - Paste a YouTube link
   - Click **Generate Reels**
   - Preview or Download reels

---

## 📋 Requirements

The `requirements.txt` file includes:

```
streamlit
yt-dlp
moviepy
openai-whisper
transformers
torch
ffmpeg-python
pyngrok
```

---

## 🎥 Demo

Example placeholder:
```
https://drive.google.com/file/d/<YOUR_VIDEO_ID>/view
```

---

## 📤 Output Format

You will get:
```
reel_1.mp4
reel_2.mp4
reel_3.mp4
...
```

Each reel contains a **high-impact emotional moment** extracted from the original video.

---

## 🏗 Future Enhancements

- Vertical auto-cropping (MediaPipe)
- Dynamic captions (karaoke style)
- Topic-based clip grouping
- Hook headline generation
- Cloud deployment (Render / HF Spaces)

---

## 👤 Author

**Aswath Raja R**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.