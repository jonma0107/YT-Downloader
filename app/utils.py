from pytube import YouTube
import os

def download_video(video_url, save_path):
  try:
    yt= YouTube(video_url)
    video_stream= yt.streams.get_highest_resolution()
    video_stream.download(output_path=save_path)
    print("Download completed!")
    return video_stream.default_filename
  except Exception as e:
    print("Error: ", str(e))

# video_link = "https://youtu.be/jVD9ZmWxhX8"
# # save_path = "C:/Users/jonma0107/Downloads"  
# save_path = os.path.expanduser("~/Downloads")  

# download_video(video_link, save_path)