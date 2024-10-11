from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess
from get_best_resolution import select_best_res

# url of the video to be downloaded
url = "https://www.youtube.com/watch?v=DhCYfOiDUEw&ab_channel=SonyMusicSouthVEVO"

# Create a Youtube Object.
yt = YouTube(url, on_progress_callback=on_progress)
title = yt.title

# selecting and printing the best available resolution, with a cap of 1080p
best_resolution = select_best_res(yt).resolution
print('Downloading in', best_resolution)

# Downloading the video file in .mp4 format
video = yt.streams.filter(resolution=best_resolution).first()
if video:
    print('Downloading Video...', yt.title)
    video.download(filename='video.mp4')
else:
    pass

# Downloading the audio file in .mp3 format
audio = yt.streams.filter(only_audio=True).first()
if audio:
    print('Downloading Audio...', yt.title)
    audio.download(filename='audio.mp3')
else:
    pass

p = subprocess.run("ffmpeg -i video.mp4 -i audio.mp3 -c copy output.mp4", stdout=subprocess.PIPE, shell=True)