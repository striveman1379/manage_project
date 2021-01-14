from django.shortcuts import render,HttpResponse

from django.conf import settings
from utils.tencent.sms import send_sms_single
# Create your views here.
import random

# def send_sms(request):
def send_sms(request):
    """
    发送短信功能
    tpl = login         842634
    tpl = register      842633
    :param request:
    :return:
    """
    # tpl = request.GET.get('tpl')
    # template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    template_id = 842633
    if not template_id:
        return HttpResponse("模板不存在")

    code = random.randrange(1000, 9999)
    res = send_sms_single('13520445436',template_id,[code,])
    if res['result'] == 0:
        return HttpResponse("成功")
    else:
        return HttpResponse(res['errmsg'])







