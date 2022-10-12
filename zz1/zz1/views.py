from django.http import HtttpResponse

def hello(request):
    return HtttpResponse("Hello,world!")