# i have created this file - sourav 
from django.http import HttpResponse
from django.shortcuts import render

def index(request) : 
    params = {'name':'Sourav','place' : 'mars'}
    return render(request,'index.html',params)

def about(request) : 
    return HttpResponse("about sourav bhai")

def personal_navigator(request) : 
    return HttpResponse(''' <h1>Personal navigator</h1>
                        <a href="https://www.youtube.com/watch?v=fQgyVwN0gAI">Bhojpuri song</a>
                        <a href="https://github.com/souravkumar31cse">My github repo</a>
                        ''')


def analyze(request) :
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')
    
    if removepunc == "on" :
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext :
            if char not in punctuations :
                analyzed = analyzed + char 
        params = { 'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on") :
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()
        params = { 'purpose':'Changed to Uppercase ','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover == "on") :
        analyzed = ""
        for char in djtext :
            if char!="\n" :
                analyzed = analyzed + char
        params = { 'purpose':'Removed NewLine ','analyzed_text':analyzed}
        djtext = analyzed
    
    if(extraspaceremover == "on") :
        analyzed = ""
        for index,char in enumerate(djtext) :
            if not (djtext[index] == " " and djtext[index+1]) == " ":
                analyzed = analyzed + char
        params = { 'purpose':'Removed NewLine ','analyzed_text':analyzed}
        djtext = analyzed

    if(charactercounter == "on") :
        analyzed = ""
        count = 0
        for char in djtext :
            count=count+1
        params = { 'purpose':'character count is ','analyzed_text':count}
    if(charactercounter!="on" and extraspaceremover!="on" and newlineremover!="on" and removepunc!="on" and fullcaps!="on") :
        return HttpResponse("Please select the operation ")

    return render(request,'analyze.html',params)
