from flask import Flask, send_file
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def extract_subtitles():
    video_url = "https://example.com/sample-video.mp4"
    output_file = "output.srt"

    try:
        # Run ffmpeg to extract the first subtitle track
        subprocess.run([
            "ffmpeg", "-i", video_url, "-map", "0:s:0",
            output_file, "-y"
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return send_file(output_file, as_attachment=True)

    except subprocess.CalledProcessError as e:
        return f"<h3>❌ FFmpeg failed:</h3><pre>{e.stderr.decode()}</pre>"

    finally:
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
