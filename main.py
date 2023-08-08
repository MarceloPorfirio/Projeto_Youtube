from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=pOnp32WlU3U"

yt = YouTube(url)

video = yt.streams.get_highest_resolution()
video.download()
