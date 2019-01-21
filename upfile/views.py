import re
import time

import os

from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Files

from untitled import settings


def index(request):
    return render(request,'index.html',locals())

@csrf_exempt
def upload(request):
    file_obj = request.FILES.get('upfile')
    # 文件保存路径
    if file_obj:
        accessory_dir = settings.accessory_dir
        if not os.path.isdir(accessory_dir):
            os.mkdir(accessory_dir)
        upload_file = "%s/%s" % (accessory_dir, file_obj.name)
        with open(upload_file, 'wb') as pic:
            for c in file_obj.chunks():
                pic.write(c)
        fileName = file_obj.name


        return JsonResponse({"msg":[{"d":fileName},{"m":"b.txt"}]})

#处理连接数据库的ajax上传文件
@csrf_exempt
def upmysql(request):

    if request.method == "POST":
        ana = request.POST.get("pname")
        version = request.POST.get("version")
        pFile = request.FILES.get("pfile")
        if pFile:
            text = Files()
            text.ana = ana
            text.version = version
            text.pFile = pFile
            text.save()
            return JsonResponse({"analy":ana,"he":"hello"})
        else:
            return JsonResponse({"analy":"失败","he":"hello"})
    else:
        return render(request,"upmysql.html")




