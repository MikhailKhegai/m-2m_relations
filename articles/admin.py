from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

class RelationshipScopeInline(admin.TabularInline):
    model = Scope
    extra = 3


@admin.register(Article)
class ArticleAdminObject(admin.ModelAdmin):
    inlines = [RelationshipScopeInline,]
