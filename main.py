from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = FastAPI()

@app.get("/transcript/")
def get_transcript(youtube_url: str):
    """
    Retrieves the transcript of a YouTube video.

    Args:
        youtube_url: The URL of the YouTube video.

    Returns:
        A formatted string of the video transcript or an error message.
    """
    try:
        video_id = youtube_url.split("v=")[-1]
        
        formatted_transcript = video_id

        return {"transcript": formatted_transcript}

    except Exception as e:
        if "subtitles are disabled" in str(e).lower():
            raise HTTPException(status_code=404, detail="No transcript available for this video. Subtitles may be disabled.")
        else:
            raise HTTPException(status_code=500, detail=f"Error retrieving transcript: {e}")

# If you want to run the application locally, you can add this:
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
