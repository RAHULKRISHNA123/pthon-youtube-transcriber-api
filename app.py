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

        # List available transcripts (languages and types)
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Choose a transcript (you can modify this to select a specific language)
        transcript = None
        try:
            # Try to get the transcript in the default language (or choose 'en' for English)
            transcript = transcript_list.find_transcript(['en'])
        except:
            # If not found, try the auto-generated transcript
            transcript = transcript_list.find_generated_transcript(['en'])

        formatted_transcript = transcript.fetch()

        return jsonify({"transcript": formatted_transcript})

    except Exception as e:
        return jsonify({"error": f"Error retrieving transcript: {e}"}), 500
