from django import forms
from posts.models import Tag
from posts.models import Post
class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'поиск...'})
    )

    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    orderings = forms.ChoiceField(
        required=False,
        choices=[
            ('title', 'Заголовок'),
            ('-title', 'Заголовок в обратном порядке'),
            ('created_at', 'Дата создания'),
            ('-created_at', 'Дата создания в обратном порядке'),
            ('updated_at', 'Дата обновления'),
            ('-updated_at', 'Дата обновления в обратном порядке'),
            ('rate', 'Рейтинг'),
            ('-rate', 'Рейтинг в обратном порядке'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'rate', 'content', 'image')
