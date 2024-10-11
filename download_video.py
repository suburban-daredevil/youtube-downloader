from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess
import os
from get_best_resolution import select_best_res

def download_video(video_url, directory_path):
    # Create a Youtube Object.
    yt = YouTube(video_url, on_progress_callback=on_progress)
    title = yt.title.replace(' ', '-')
    video_name = f'{title}_video.mp4'
    audio_name = f'{title}_audio.mp3'
    output_name = f'{title}.mp4'

    # selecting and printing the best available resolution, with a cap of 1080p
    best_resolution = select_best_res(yt).resolution
    print('Downloading in', best_resolution)

    # Downloading the video file in .mp4 format
    video = yt.streams.filter(resolution=best_resolution).first()
    if video:
        print('Downloading Video...', yt.title)
        video.download(filename=video_name)
    else:
        pass

    # Downloading the audio file in .mp3 format
    audio = yt.streams.filter(only_audio=True).first()
    if audio:
        print('Downloading Audio...', yt.title)
        audio.download(filename=audio_name)
    else:
        pass
    path_to_save = directory_path + '/' + output_name
    cmd = f"ffmpeg -i {video_name} -i {audio_name} -c copy {path_to_save}"
    print(cmd)
    p = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

    # delete the unwanted files
    os.remove(video_name)
    os.remove(audio_name)