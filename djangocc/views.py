from django.shortcuts import render

def home(request):
    '''
    Renders home page
    '''
    greeting = "uStudy - the best study site in the world!"
    today = 'tuesday'
    # a dictionary with a keyword 'our_greeting' mapping to the variable greeting defined above.
    context = {'our_greeting':greeting, 'day_of_week':today} #an empty dictionary
    return render(request, 'home.html', context)
