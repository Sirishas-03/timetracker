from django.shortcuts import render
from django.http import HttpResponse
import datetime
def current_datetime(request):
 now = datetime.datetime.now()
 html = f"<html><body>Current date and time: {now.strftime('%d- %m-%Y %:%M:%S')}</body></html>"
 return HttpResponse(html)