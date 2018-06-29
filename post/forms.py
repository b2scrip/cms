from .models import Post
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ['title','content','catalog','img',]
        help_texts = {
        "content":"1000",
        }
    def clean_content(self):
        if self.cleaned_data['content'] == "":
            return forms.ValidationError('ERROR_ACCOUNT_EXISTED')
        return self.cleaned_data['content']
