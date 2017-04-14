from django import forms
from .models import Comment


class EmailPost(forms.ModelForm):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    send_to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentFor(forms.ModelForm):


    class Meta:
        model=Comment
        fields=('name','email','body')



