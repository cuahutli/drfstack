from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from bs4 import BeautifulSoup

import requests
import json

# Create your views here.


def index(request):
    return HttpResponse("Welcome to API StackOverflow ")

def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")

        soup = BeautifulSoup(res.text, "html.parser")

        questions = soup.select(".question-summary")
        for que in questions:
            q = que.select_one('.question-hyperlink').getText()
            vote_count = que.select_one('.vote-count-post').getText()
            views = que.select_one('.views').attrs['title']
            tags = [i.getText() for i in (que.select('.post-tag'))]

            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags

            question.save()
        return HttpResponse("Latest Data Fetched from Stack Overflow")
    except e as Exception:
        return HttpResponse(f"Failed {e}")
