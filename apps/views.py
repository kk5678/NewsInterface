from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from apps.pachong.TYnews import result_news

# Create your views here.
@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == 'GET':
        dic['message'] = 0
        dic['status']=HttpResponse.status_code
        dic['TYnewslist']=result_news()
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))
