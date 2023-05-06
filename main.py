from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
ID = input("Youtube Video URL: ").split('?v=')[1].lstrip().split('&')[0]
print('\n',TextFormatter().format_transcript(YouTubeTranscriptApi.get_transcript(ID)).replace('\n', ' '))
input("\nCopy the text, then press ENTER to exit...")