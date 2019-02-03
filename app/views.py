"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import RequestContext
from datetime import datetime
from .ftpclient import FtpClient
import json

from .forms import ConnectionForm

def home(request):
    """Renders the home page."""
    form = ConnectionForm(request.POST or None)
    ftp = FtpClient()
    if request.method == 'POST':
        if form.is_valid():
            request.session['isLogged'] = True

            request.session['server'] = request.POST.get('server')
            if request.POST.get('username'):
                request.session['username'] = request.POST.get('username')
            else:
                request.session['username'] = None
            if request.POST.get('password'):
                request.session['password'] = request.POST.get('password')
            else:
                request.session['password'] = None
            if request.POST.get('port') == None:
                request.session['port'] = request.POST.get('port')
            else:
                request.session['port'] = 21

            """ftp = FTP(request.POST.get('server'))
            ftp.login(request.POST.get('username'), request.POST.get('password'))
            print(ftp.retrlines('LIST'))
            ftp.quit()"""

    assert isinstance(request, HttpRequest)
    if request.session.get('isLogged') == True:
        ftp.connectToServer(request.session.get('server'), request.session.get('username'), request.session.get('password'), request.session.get('port'))
        #ftp.list()
        return render(
            request,
            'app/home.html'
        )
    else:
        return render(
            request,
            'app/login.html',
            {'form': form}
        )

def disconnect(request):
    request.session.modified = True
    del request.session['isLogged']
    del request.session['server']
    del request.session['username']
    del request.session['password']
    del request.session['port']
    return HttpResponseRedirect('/')

def json_event(request):
    ftp = FtpClient()
    ftp.connectToServer(request.session.get('server'), request.session.get('username'), request.session.get('password'), request.session.get('port'))
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        if data["action"] == "disconnect":
            return JsonResponse({"action": "goto_disconnect"})
        elif data["action"] == "pwd":
            return JsonResponse({"message": ftp.pwd()})
        elif data["action"] == "get_list":
            return JsonResponse({"message": ftp.list()})
        return HttpResponse("OK");
