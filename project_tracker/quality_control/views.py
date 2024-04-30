from django.shortcuts import render, redirect
from .models import BugReport, FeatureRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.urls import reverse
from .forms import BugReportForm, FeatureRequestForm

def index(request):
    return render(request, 'quality_control/index.html')

class IndexView(View):
    def get(self, request):
        html = "<h1>Система контроля качества. CBV представление.</h1>"
        html += "<a href='/quality_control/bugs/'>Список всех багов</a>"
        html += "<a href='/quality_control/features/'>Запросы на улучшение</a>"
        return HttpResponse(html)

def bug_list(request):
     bugs = BugReport.objects.all()
     return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class FeatureRequestDetailView(DetailView):
     model = FeatureRequest
     pk_url_kwarg = 'feature_id'
     template_name = 'quality_control/feature_detail.html'
     context_object_name = 'feature'



def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()

    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()

    return render(request, 'quality_control/feature_request_form.html', {'form': form})
