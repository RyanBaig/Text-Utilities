# I have created this file - Ryan


#                   EXERCISE
# def pn(request):
#    return HttpResponse("""
#    
#    <h1 align="center">Personal Navigator</h1>
#    <h2 align="center">Links:</h2>
#    <ul>
#        <li><a href="https://github.com">GitHub</a></li>
#        <li> <a href="https://youtube.com">YouTube</a></li>
#        <li><a href="https://chat.openai.com/chat">ChatGPT</a></li>
#        <li><a href="https://www.google.com/">Google</a></li>
#    </ul>
#    """)

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
#    return HttpResponse("Hello World!")
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check the values of the functions
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchars = request.POST.get('countchars', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = """!()-[]{}:;'"\,<>./?@#$%^&*_~"""
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed


    elif fullcaps == "on":
        analyzed = ''
        analyzed = djtext.upper()
        params = {
            "purpose": "Changed to Uppercase",
            "analyzed_text": analyzed
        }
        djtext = analyzed


    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


    elif extraspaceremover=="on":
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

    
    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on":
        return HttpResponse("Error! Please select any operation and try again!")

    return render(request, 'analyze.html', params)

