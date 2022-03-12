from django import forms
from .models import *

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='заголовок', widget=forms.TextInput(attrs={'class': 'input-group flex-nowrap'}))
#     slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'input-group flex-nowrap'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_pub = forms.BooleanField(required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="НЕ выбрана")

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Cake
        fields = ['title', 'slug', 'content', 'is_pub', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-group flex-nowrap'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 5})
        }
