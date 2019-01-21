from django.conf.urls import url
from . import views
app_name = "upfile"
urlpatterns = [
    url(r"^$",views.index,name = "index"),
    url(r"^upload/$",views.upload,name = "upload"),
    url(r"^upmysql/$",views.upmysql,name = "upmysql"),
]