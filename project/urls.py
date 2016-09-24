from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^studentDB/', include("teachers.urls")),
    url(r'^copo/', include("copo.urls")),
]
