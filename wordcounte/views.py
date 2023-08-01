from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>This is a word counter</h1>')


def noaa(request):
    return HttpResponse('<h1>Page Not Found</h1>')

def count(request):
    fulltext = request.GET['fullText']

    wordlist = fulltext.split()

    worddictonary = {}

    for word in wordlist:
        if word in worddictonary:
            #increase
            worddictonary[word] += 1

        else:
            #add to dictonary
            worddictonary[word] = 1
    sortedwords= sorted(worddictonary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords})
