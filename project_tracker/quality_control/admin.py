from django.contrib import admin
from .models import BugReport, FeatureRequest

# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'status', 'priority')
        }),
    )

    actions = ['change_status']

    def change_status_completed(self, request, queryset):
        new_status = request.POST.get('new_status', 'Completed')
        for bug_report in queryset:
            bug_report.status = new_status
            bug_report.save()

    change_status_completed.short_description = 'Change status to "Completed"'

    def change_status_new(self, request, queryset):
        new_status = request.POST.get('new_status', 'New')
        for bug_report in queryset:
            bug_report.status = new_status
            bug_report.save()

    change_status_new.short_description = 'Change status to "New"'

    def change_status_progress(self, request, queryset):
        new_status = request.POST.get('new_status', 'In_progress')
        for bug_report in queryset:
            bug_report.status = new_status
            bug_report.save()

    change_status_progress.short_description = 'Change status to "In_progress"'


# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'status', 'priority')
        }),
    )
