from django import forms
from .models import Article, Category


class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

            self.fields['category'].choices = friendly_name
