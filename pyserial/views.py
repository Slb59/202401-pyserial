from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, "index.html")


def current_time(request):
    current_date_time = datetime.datetime.now()
    return HttpResponse(f"The Current time: {current_date_time}")

# from django.shortcuts import get_object_or_404, render_to_response
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
# from django.template import RequestContext
# from forms import SearchForm
# from arduino.arduinoMorse import ArduinoMorse
# from threading import Thread
# from firmata import *
# a = Arduino('/dev/ttyUSB0')
# a.pin_mode(13, firmata.OUTPUT)
# def dot():
#     a.digital_write(13, firmata.HIGH)
#     a.delay(0.5)
#     a.digital_write(13, firmata.LOW)
#     a.delay(0.5)
# def slash():
#     a.digital_write(13, firmata.HIGH)
#     a.delay(1.5)
#     a.digital_write(13, firmata.LOW)
#     a.delay(0.5)
# ...
# class ArduinoMorse (Thread):
#     def __init__(self, text):
#         Thread.__init__(self)
#         self.text=text
#     def run(self):
#             for x in self.text :
#                 if x=='a' or x=='A':
#                     dot()
#                     slash()
#                     spaceL()
#                 ...
#                 eLif x=='z' or x=='Z':
#                 ... 
# def encode(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             text = form.cleaned_data['text']
#             arduino=ArduinoMorse(text)
#             arduino.start()
#         else:
#             queryset = []
#     form = SearchForm()
#     return render_to_response("arduino/index.html", {'form': form})
