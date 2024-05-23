import yt_dlp
import os

def download_audio(url, destination='.', ffmpeg_location=None, ffprobe_location=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s')
    }
    
    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location

    if ffprobe_location:
        ydl_opts['ffprobe_location'] = ffprobe_location

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

try:
    url = str(input("Enter the URL of the video you want to download: \n>> "))
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
    
    ffmpeg_location = r # CESTA K "C:\.\ffmpeg-7.0-essentials_build\bin\ffmpeg.exe"
    ffprobe_location = r # CESTA K "C:\.\ffmpeg-7.0-essentials_build\bin\ffprobe.exe"
    
    download_audio(url, destination, ffmpeg_location, ffprobe_location)
    print("Download completed successfully.")
except Exception as e:
    print(f"Error: {e}")
