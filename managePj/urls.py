# -*- coding:utf-8 -*-
from django.conf.urls import url,include

from managePj.views import send_sms

urlpatterns = {
    url(r'^send/sms/$',send_sms)
}