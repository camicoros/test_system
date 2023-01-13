from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

from adminsortable2.admin import SortableAdminMixin
from tinymce.widgets import TinyMCE

from .models import TestSet, TestQuestion, Answer


class TestSetForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = TestSet
        fields = '__all__'


@admin.register(TestSet)
class TestSetAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug')
        }),
        (_('Date options'), {
            # 'classes': ('collapse',),
            'fields': ('created', 'updated'),
        }),
    )
    form = TestSetForm
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'sort_order')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('test_set', 'question', 'slug', 'several_correct_answers')
        }),
        (_('Date options'), {
            'fields': ('created', 'updated'),
        }),
    )
    readonly_fields = ('created', 'updated')
    list_display = ('question', 'test_set', 'several_correct_answers')
    prepopulated_fields = {'slug': ('question', )}


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('question', 'answer', 'is_correct')
        }),
        (_('Date options'), {
            'fields': ('created', 'updated'),
        }),
    )
    readonly_fields = ('created', 'updated')
    list_display = ('answer', 'question', 'is_correct')
