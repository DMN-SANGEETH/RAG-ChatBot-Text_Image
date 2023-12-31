from django.shortcuts import render
from django.http import HttpResponse
from model.model import get_response
from . import greet, greetList

# Create your views here.


def index(request):
    return render(request, 'gcore/index.html')

def specific(request):
    return HttpResponse("This is specific url")

def getRespones(request):
    userMessage = request.GET.get('userMessage')

    if userMessage.lower() in greetList:
        predefined_response = greet.get_predefined_response(userMessage)
        return HttpResponse(predefined_response)
    else:
        result = get_response(userMessage)
        return HttpResponse(result)


'''def article(request, article_id):
    return HttpResponse(article_id)
    '''
'''def article(request, article_id):
    return render(request, 'blog/index.html', {'article_id':article_id})
    '''