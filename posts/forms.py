

from django import forms
from posts.models import Tag

class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'поиск...'}
                               ))

    tags = forms.ModelMultipleChoiceField(required=False,
                                          queryset=Tag.objects.all(),
                                          widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    orderings = {
        ('title', 'заголовок'),
        ('-title', 'заголовок в обратном порядке'),
        ('create_at', 'дата создания'),
        ('-create_at', 'дата создания в обратном порядке'),
        ('updated_at', 'дата обновления'),
        ('-updated_at', 'дата обновления в обратном порядке'),
        ('rate', 'рейтинг'),
        ('-rate', 'рейтинг в обратном порядке'),
    }
    orderings = forms.CharField(required=False, choices=orderings, widget=forms.Select(attrs={'class': 'form-control'}))
