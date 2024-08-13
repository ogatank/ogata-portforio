from django import forms
from .models import BlogPost, Tag
from ckeditor.widgets import CKEditorWidget

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # CKEditorWidgetを使用

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags', 'image']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

