from django import forms
from .models import Article, Category
from tinymce.widgets import TinyMCE


class ArticleForm(forms.ModelForm):

    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta():
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
