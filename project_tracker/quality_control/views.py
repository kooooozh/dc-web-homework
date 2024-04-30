from django.shortcuts import render, redirect
from .models import BugReport, FeatureRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .forms import BugReportForm, FeatureRequestForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')

class BugReportListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'
    context_object_name = 'bug_list'

class BugReportCreateView(CreateView):
    model = BugReport
    template_name = 'quality_control/bug_report_form.html'
    fields = '__all__'
    success_url = reverse_lazy('quality_control:bug_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    template_name = 'quality_control/bug_update.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'pk': self.object.pk})

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_confirm_delete.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'feature_list'

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_form.html'
    fields = '__all__'
    success_url = reverse_lazy('quality_control:feature_list')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    template_name = 'quality_control/feature_update.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'pk': self.object.pk})

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'quality_control/feature_confirm_delete.html'
    success_url = reverse_lazy('quality_control:feature_list')
