from .models import Post,Comment
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
            'parent'
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self['content'].field.widget.attrs['rows'] = 5
        self['content'].field.widget.attrs['size'] = 5
        self['parent'].field.widget = forms.HiddenInput()
    def clean_content(self):
        data =  self.cleaned_data['content']
        if len(data) > 500:
            raise forms.ValidationError("Comment short be shorter")
        return data
