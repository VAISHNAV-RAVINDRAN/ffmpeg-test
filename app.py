from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def check_ffmpeg():
    """
    When you visit the root URL, this will check if FFmpeg
    is installed and display its version info.
    """
    try:
        # Run "ffmpeg -version" to check installation
        result = subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        version_info = result.stdout.decode()
        return f"""
        <h2>✅ FFmpeg is installed and working!</h2>
        <pre>{version_info}</pre>
        """
    except Exception as e:
        return f"""
        <h2>❌ FFmpeg is not installed or failed to run.</h2>
        <pre>{str(e)}</pre>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
