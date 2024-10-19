# prompt: generate code to get transcript of a youtube video with the input as the yoututbe video link

!pip install youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(youtube_url):
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
    print(f"Error retrieving transcript: {e}")
    return None

# Example usage
youtube_url = "https://www.youtube.com/watch?v=inN8seMm7UI"  # Replace with your YouTube video URL
transcript = get_transcript(youtube_url)

if transcript:
  for segment in transcript:
    print(f"{segment['text']}")
else:
  print("No transcript found for this video.") 
