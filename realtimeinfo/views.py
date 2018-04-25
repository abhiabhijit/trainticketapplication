from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from .forms import Detail

def index(request):
    if request.method == 'POST':
        print(request.POST)
        # form = Detail(request.POST)
        # if form.is_valid():
        #
        #
        #     return HttpResponse('New Password sent to your email address.')
    else:
        form = Detail()
    return render(request,"home.html",{})


# # Create your views here.
# # def autocomplete(request):
# #     if request.is_ajax():
# #         re = requests.get(
# #             "https://api.railwayapi.com/v2/suggest-station/name/mum/apikey/dp9sdxkesa/")
# #         data = re.json()
# #         return JsonResponse(data)