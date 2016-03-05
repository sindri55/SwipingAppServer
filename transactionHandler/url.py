from django.conf.urls import url
from transactionHandler import api

urlpatterns = [
    url(r'^register', api.registerUser),
    url(r'^login', api.user_login),
    url(r'^logout', api.user_logout),
    url(r'^profile', api.user_profile),
]
