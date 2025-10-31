from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def extract_subtitles():
    # ✅ Direct Dropbox video URL
    video_url = "https://www.dropbox.com/scl/fi/3p351jeju63np8ez371fx/Let-s-Learn-English-on-the-Road-_-English-Video-with-Subtitles.mp4?rlkey=a96sz8karrv56bsf5m7j3ppap&st=ck7wuhkc&raw=1"

    output_file = "output.srt"

    try:
        # Run ffmpeg command to extract the first subtitle track
        result = subprocess.run([
            "ffmpeg", "-y", "-i", video_url, "-map", "0:s:0", output_file
        ], check=True, capture_output=True, text=True)

        if os.path.exists(output_file):
            return send_file(output_file, as_attachment=True)
        else:
            return "<h3>❌ Subtitle file not found — maybe no subtitles in this video.</h3>"

    except subprocess.CalledProcessError as e:
        return f"<h3>❌ FFmpeg failed:</h3><pre>{e.stderr}</pre>"

    finally:
        # Clean up temporary file if it exists
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
