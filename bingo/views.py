from django.shortcuts import render

# Create your views here.
from bingo.models import *
from django.http import HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
import datetime


def home(request):
    articles = Article.objects.all()
    return render_to_response("bingo/index.html", Context({"articles": articles}))


def get_article(request, article_id):
    article = Article.objects.filter(id=article_id)

    if article.exists():
        print(article[0])
        return render_to_response("bingo/post.html", Context({'article': article[0]}))
    else:
        raise Http404


def get_about_me(request):
    about_me = AboutMe.objects.all()

    if about_me:
        return render_to_response("bingo/about.html", Context({'about_me': about_me[0]}))
    else:
        return render_to_response("bingo/about.html", Context({'about_me': about_me}))


def contact_me(request):
    return render_to_response("bingo/contact.html")