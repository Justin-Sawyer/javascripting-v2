from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    context = {
        'title': 'JavaScripting : The Home Page.',
        'pagename': 'Home.',
        'script': f'https://www.yourjs.com/console/?code=console.log%28%27This+is+a+console+payground.+Enter+your+code+here%21%27%29%3B&dontRunLastBreak=1',
        'data_slug_hash': 'OJjRYxX'
    }
    return render(request, 'home/index.html', context)

