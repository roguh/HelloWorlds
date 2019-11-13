from django.http import HttpResponse

template = '''<html>
    <head>
        <title>HELLO-WORLD SERVER</title>
    </head>
    <body>
        <h1>Hello</h1>
        <p>{}!</p>
    </body>
    </html>
'''

def index(request):
    return HttpResponse(template.format('world'))
