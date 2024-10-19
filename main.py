from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/transcript/")
def get_transcript(youtube_url: str):
    """
    Retrieves the transcript of a YouTube video.

    Args:
        youtube_url: The URL of the YouTube video.

    Returns:
        A list of dictionaries, where each dictionary represents a segment of the 
        transcript with 'text' and 'start' keys.
        Returns None if no transcript is found.
    """
    try:
        video_id = youtube_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving transcript: {e}")

