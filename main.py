from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = Flask(__name__)

@app.route('/transcript/', methods=['GET'])
def get_transcript():
    """
    Retrieves the transcript of a YouTube video.

    Args:
        youtube_url: The URL of the YouTube video.

    Returns:
        A formatted string of the video transcript or an error message.
    """

    youtube_url = request.args.get('youtube_url')
     if not youtube_url:
        return jsonify({"error": "YouTube URL is required"}), 400

    try:
        video_id = youtube_url.split("v=")[-1]

        # Retrieve the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        formatted_transcript = transcript

        return jsonify({"transcript": formatted_transcript})

    except Exception as e:
        if "subtitles are disabled" in str(e).lower():
            return jsonify({"error": "No transcript available for this video. Subtitles may be disabled."}), 404
        else:
            return jsonify({"error": f"Error retrieving transcript: {e}"}), 500

# If you want to run the application locally, you can add this:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
