from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Dtapp

# Create your views here.
#get all attendees frome the db and return them to d template
def current_time(request):
    dtapp = Dtapp.objects.all()
    
    return render(request, "dtapp/index.html", {"dtapp": dtapp})




#def current_time(request):
 #   now = datetime.datetime.now()
  #  html = "<html><body>It is now %s.</body></html>" % now
   # return HttpResponse(html)
