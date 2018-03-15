from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^pwd_reset/', include('password.urls', namespace='pwd_reset')),
]
