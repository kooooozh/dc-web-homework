from django.shortcuts import render
from .models import BugReport, FeatureRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    html = "<h1>Система контроля качества</h1>"
    html += "<a href='/quality_control/bugs/'>Список всех багов</a>"
    html += '<br></br>'
    html += "<a href='/quality_control/features/'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    html = "<h1>Cписок отчетов об ошибках</h1>"
    bugs = BugReport.objects.all()
    for bug in bugs:
        html += f"<p>{bug.title} - {bug.project} - {bug.status} - {bug.priority} - {bug.created_at}</p>"
    return HttpResponse(html)

def feature_list(request):
    html = "<h1>Список запросов на улучшение</h1>"
    features = FeatureRequest.objects.all()
    for feature in features:
        html += f"<p>{feature.title} - {feature.project} - {feature.status} - {feature.priority} - {feature.created_at}</p>"
    return HttpResponse(html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    html = f"<h1>Детали бага {bug_id}</h1>"
    html += f"<p>Название: {bug.title}</p>"
    html += f"<p>Описание: {bug.description}</p>"
    html += f"<p>Проект: {bug.project}</p>"
    html += f"<p>Статус: {bug.status}</p>"
    html += f"<p>Приоритет: {bug.priority}</p>"
    html += f"<p>Дата создания: {bug.created_at}</p>"
    html += f"<p>Дата обновления: {bug.updated_at}</p>"
    return HttpResponse(html)

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    html = f"<h1>Детали улучшения {feature_id}</h1>"
    html += f"<p>Название: {feature.title}</p>"
    html += f"<p>Описание: {feature.description}</p>"
    html += f"<p>Проект: {feature.project}</p>"
    html += f"<p>Статус: {feature.status}</p>"
    html += f"<p>Приоритет: {feature.priority}</p>"
    html += f"<p>Дата создания: {feature.created_at}</p>"
    html += f"<p>Дата обновления: {feature.updated_at}</p>"
    return HttpResponse(html)
