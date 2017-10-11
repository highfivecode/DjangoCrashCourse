from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome there to our first django app! Powered by Python and the Django Crash Course.')
