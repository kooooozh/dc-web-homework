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

    def change_status(self, request, queryset):
        new_status = request.POST.get('new_status', 'Completed')
        for bug_report in queryset:
            bug_report.status = new_status
            bug_report.save()

    change_status.short_description = 'Change status to "Completed"'


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
