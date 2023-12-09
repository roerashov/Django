from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import *


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        data = []
        for form in self.forms:
            cl_data = form.cleaned_data
            if cl_data.get('is_main'):
                data.append(cl_data['is_main'])
        if data.count(True) > 1:
            raise ValidationError('Должен быть только один основной тэг')
        elif data.count(True) < 1:
            raise ValidationError('Должен быть хотя бы один основной тэг')
        print(data)
        return super().clean()


class Scopesinline(admin.TabularInline):
    model = Scopes
    formset = RelationshipInlineFormset
    extra = 3


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']
    


@admin.register(Article)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [Scopesinline, ]
