from django import forms
from .models import Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['author', 'text', 'image', 'title']

        widgets = {
                'author' : forms.Select(attrs={
                    'class': "form-control",
                    'style': 'max-width: 300px;'}),
                'title': forms.TextInput(attrs={'class': 'form-control', 
                                                'placeholder': 'Заголовок блога', 
                                                'required': 'required'}),
                'image': forms.FileInput(attrs={'class': 'form-control', 
                                                'label': 'Изображение',
                                                'required': 'required',}),
                'text': forms.Textarea(attrs={  'class': 'form-control', 
                                                'required': 'required',
                                                'placeholder': 'Контент'
                                                    }),
                
            }