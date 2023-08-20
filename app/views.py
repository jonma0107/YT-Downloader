from django.shortcuts import render
from .utils import download_video
from pytube import YouTube
import os

from django.http.response import HttpResponse
import mimetypes

# Create your views here.
def download_view(request):
  message = None
  if request.method == 'POST':
    video_link = request.POST['video_link']
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    save_path = os.path.join(BASE_DIR, 'downloaded_videos')  # Carpeta de descarga
    filename = download_video(video_link, save_path)
    file_path = os.path.join(save_path, filename)

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
      response = HttpResponse(content_type=mime_type)
      response['Content-Disposition'] = f"attachment; filename={filename}"
      with open(file_path, 'rb') as video_file:
        response.write(video_file.read())
      return response
    else:
      message = "Error: MIME type not found."  
  return render(request, 'download.html', {'message': message})  