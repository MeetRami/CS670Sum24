from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi 

def videoDownload(link):
    ytObj = YouTube(link)
    ytObj = ytObj.streams.get_highest_resolution()
    try:
        ytObj.download()
    except:
        print("An error has occurred")
    print("Video download is completed successfully")

def videoTranscript(link):
    videoID = link.split('/')[-1]
    sub = YouTubeTranscriptApi.get_transcript(videoID)
    with open("subtitles.txt", "w") as f:
        for i in sub:
            f.write("{}\n".format(i))
    print("Subtitles download is completed successfully")

link = input("Enter the YouTube video URL: ")
videoDownload(link)
videoTranscript(link)