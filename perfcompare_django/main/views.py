from django.shortcuts import render

def index(request):
    resp = render(request, 'main/index.html', {'title': 'hey'})
    resp['Access-Control-Allow-Origin'] = 'http://perfcompare.herokuapp.com'
    return resp
