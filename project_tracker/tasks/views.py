from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    another_page_url = reverse('tasks:another_page')
    html = f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a>"
    html += '<br></br>'
    html += f"<a href='/quality_control/'>Страница приложения quality_control</a>"
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")