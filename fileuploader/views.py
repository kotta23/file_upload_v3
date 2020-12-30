import os
from django.shortcuts import render
from django.conf import settings
from .models import DesignFile
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def download_latest_design(request):
    latest_file = DesignFile.objects.filter(done=False).last()
    if latest_file:
        abs_path = os.path.join(settings.MEDIA_ROOT,latest_file.file.path)
        if os.path.exists(abs_path):
            with open(abs_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                print(response)
                response['Content-Disposition'] = 'filename=' + os.path.basename(abs_path)
                print(response['Content-Disposition'])
                response['file_id'] = f"{latest_file.pk}"
                return response
        else:
            HttpResponseNotFound("file deleted")
    return HttpResponseNotFound("no records")

def change_file_statue(request):
    try:
        file_id = request.GET.get("file_id")
        file_obj = DesignFile.objects.get(pk=file_id)
        file_obj.done= True
        file_obj.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("")

