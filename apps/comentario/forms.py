from django import forms 
from .models import Comentario
class CommentForm(forms.ModelForm):
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'2', 
            'placeholder':'Escribe un comentario...',
            }), required=True, max_length=250)
    class Meta:
        model = Comentario
        fields = ('comentario',)  
