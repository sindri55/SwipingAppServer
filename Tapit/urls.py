from django.conf.urls import url, include
from django.contrib import admin
from transactionHandler.url import urlpatterns as apiURLS

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiURLS))
]
