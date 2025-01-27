import yt_dlp

resolution='best'
save_path='.'
video_url='https://www.youtube.com/watch?v=m5YLZJj2UlA'
try:
    # Set options for yt-dlp
    ydl_opts = {
        'format': resolution,  # 'best' will get the highest resolution
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save path and file name format
        'noplaylist': True  # Avoid downloading playlists if given a playlist URL
    }

    # Download the video
    print(f"Downloading {video_url}...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f"Download complete! Saved to {save_path}")

except Exception as e:
    print(f"An error occurred: {e}")
