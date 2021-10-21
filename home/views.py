from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    context = {
        'title': 'JavaScripting : The Home Page.',
        'pagename': 'Home.'
    }
    return render(request, 'home/index.html', context)


def index2(request):
    """ A view to return the index page """
    context = {
        'title': 'JavaScripting : The Second Home Page.',
        'section': 'Section',
        'pagename': 'Second Home.'
    }
    return render(request, 'home/index2.html', context)

