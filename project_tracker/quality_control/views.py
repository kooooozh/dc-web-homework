from django.shortcuts import render
from .models import BugReport, FeatureRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse

# def index(request):
#     html = "<h1>Система контроля качества</h1>"
#     html += "<a href='/quality_control/bugs/'>Список всех багов</a>"
#     html += '<br></br>'
#     html += "<a href='/quality_control/features/'>Запросы на улучшение</a>"
#     return HttpResponse(html)

def index(request):
    return render(request, 'quality_control/index.html')

class IndexView(View):
    def get(self, request):
        html = "<h1>Система контроля качества. CBV представление.</h1>"
        html += "<a href='/quality_control/bugs/'>Список всех багов</a>"
        html += "<a href='/quality_control/features/'>Запросы на улучшение</a>"
        return HttpResponse(html)

# def bug_list(request):
#     html = "<h1>Cписок отчетов об ошибках</h1>"
#     bugs = BugReport.objects.all()
#     for bug in bugs:
#         html += f"<p>{bug.title} - {bug.status} - </p>"
#         num = bug.id
#         html += f"<a href='/quality_control/bugs/{num}/'>Посмотреть детали</a>"
#     return HttpResponse(html)


def bug_list(request):
     bugs = BugReport.objects.all()
     return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})



# def feature_list(request):
#     html = "<h1>Список запросов на улучшение</h1>"
#     features = FeatureRequest.objects.all()
#     for feature in features:
#         html += f"<p>{feature.title} - {feature.status}</p>"
#         num = feature.id
#         html += f"<a href='/quality_control/features/{num}/'>Посмотреть детали</a>"
#     return HttpResponse(html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

# class BugReportDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     def get(self, request, *args, **kwargs):
#         bug = self.get_object()
#         html = f"<h1>Детали бага {bug.id}</h1>"
#         html += f"<p>Название: {bug.title}</p>"
#         html += f"<p>Описание: {bug.description}</p>"
#         html += f"<p>Проект: {bug.project}</p>"
#         html += f"<p>Статус: {bug.status}</p>"
#         html += f"<p>Приоритет: {bug.priority}</p>"
#         html += f"<p>Дата создания: {bug.created_at}</p>"
#         html += f"<p>Дата обновления: {bug.updated_at}</p>"
#         return HttpResponse(html)

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

# class FeatureRequestDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     def get(self, request, *args, **kwargs):
#         feature = self.get_object()
#         html = f"<h1>Детали улучшения {feature.id}</h1>"
#         html += f"<p>Название: {feature.title}</p>"
#         html += f"<p>Описание: {feature.description}</p>"
#         html += f"<p>Проект: {feature.project}</p>"
#         html += f"<p>Статус: {feature.status}</p>"
#         html += f"<p>Приоритет: {feature.priority}</p>"
#         html += f"<p>Дата создания: {feature.created_at}</p>"
#         html += f"<p>Дата обновления: {feature.updated_at}</p>"
#         return HttpResponse(html)


class FeatureRequestDetailView(DetailView):
     model = FeatureRequest
     pk_url_kwarg = 'feature_id'
     template_name = 'quality_control/feature_detail.html'
     context_object_name = 'feature'
