from dataclasses import field
from django import forms
from fund_uocra_02 import settings
from .models import Comentario

class ComentarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comentario'].widget.attrs.update({'rows': '4'})

    class Meta:
        model = Comentario
        fields = ['comentario']
        exclude = ['noticia', 'autor' ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario',)
        Comentario.autor = settings.AUTH_USER_MODEL
        
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }        