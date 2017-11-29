#-*- coding: utf8 -*-
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_ckeditor.widgets import CKEditorWidget


class PageForm(ModelForm):
    class Meta:
        widgets = {
            'name': CKEditorWidget(editor_options={'startupFocus': True})
        }


class PageAdmin(ModelAdmin):
    form = PageForm
    fieldsets = [
        ('Body', {'classes': ('full-width',), 'fields': ('body',)})
    ]


admin.site.register(Page, PageAdmin)