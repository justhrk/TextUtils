# This file is made by me

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dict2 = {"name": "harshal", "age": 20}
    return render(request, "index.html", dict2)


def analyze(request):
    # get the text
    djtext = request.POST.get("text", "default")
    purpose = "No Change"
    # Check Checkbox value
    removepunc = request.POST.get("removepunc", "off")
    upper = request.POST.get("uppercase", "off")
    newl = request.POST.get("newlineremover", "off")
    space = request.POST.get("spaceremover", "off")
    chcount = request.POST.get("charcounter", "off")

    # analyze the text
    analyzed = djtext

    # Punctuation Remover
    if removepunc == "on":
        analyzed = ""
        punc = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

        for ch in djtext:
            if ch not in punc:
                analyzed += ch
        purpose = "Remove Punctuations"
        djtext = analyzed

    # All Uppercase
    if upper == "on":
        analyzed = analyzed.upper()
        purpose = "All Uppercase"
        djtext = analyzed

    # Newline Remover
    if newl == "on":
        analyzed = ""

        for ch in djtext:
            if ch != "\n" and ch != "\r":
                analyzed += ch
        purpose = "Newline Remover"
        djtext = analyzed

    # Space Remover
    if space == "on":
        analyzed = ""
        for ch in djtext:
            if ch != " ":
                analyzed += ch
        purpose = "Space Remover"
        djtext = analyzed

    # Character Counter
    if chcount == "on":
        analyzed = len(analyzed)
        purpose = "Character Counter"
        djtext = analyzed

    params = {"purpose": purpose, "analyzed_text": analyzed}
    return render(request, "analyze.html", params)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
