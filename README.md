# Youtube Transcript Exporter v0.1

Easy to use python script to copy formatted transcripts from your favorite Youtube videos

## Install
The script needs the following package:
```
pip install youtube-transcript-api
```
After installing this, just download main.py and use it

## How to use

1. Start `main.py`
2. Input your Youtube video URL
3. Copy the transcript and exit

## Code preview
There are only 5 lines of code really
```py
from youtube_transcript_api import YouTubeTranscriptApi #Import Transcript API
from youtube_transcript_api.formatters import TextFormatter #Import the text formatter
ID = input("Youtube Video URL: ").split('?v=')[1].lstrip().split('&')[0] #Get ID from URL input
print('\n',TextFormatter().format_transcript(YouTubeTranscriptApi.get_transcript(ID)).replace('\n', ' ')) #Export transcript
input("\nCopy the text, then press ENTER to exit...") #Give the user time to copy before exitting
```
