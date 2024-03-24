from django.contrib import admin
from django.utils.html import mark_safe
from django import forms
from .models import Category, Course, Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }

    form = LessonForm
    list_display = ["id", "subject","created_date","active" ,"course"]
    search_fields = ["subject", "created_date","course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]

    def avatar(self, lesson):
            return mark_safe("<img src='/static/{img_url}' width='120px'/>".format(img_url=lesson.image.name))

class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'

class CourseAdmin(admin.ModelAdmin):
    inlines =(LessonInline, )

class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY KHOA HOC TRUC TUYEN'

admin_site = CourseAppAdminSite('mycourse')

admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)