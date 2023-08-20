from django.shortcuts import render
from .utils import download_video
from pytube import YouTube
import os

# Create your views here.
def download_view(request):
  message = None
  if request.method == 'POST':
    video_link = request.POST['video_link']
    save_path = os.path.expanduser("~/Downloads")
    try:
      download_video(video_link, save_path)
      message = "Download completed!"
    except Exception as e:
      message = f"Error: {str(e)}"  
  return render(request, 'download.html', {'message': message})  