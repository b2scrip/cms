from .models import Video,VideoComment

from django import forms

class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
                 "title",
                 "iframe",
                 "catalog",
                 "img",
              ]

#    def __init__(self, *args, **kwargs):
#        super(CommentForm, self).__init__(*args, **kwargs)
#        self['content'].field.widget.attrs['rows'] = 5
#        self['content'].field.widget.attrs['size'] = 5
#        self['parent'].field.widget = forms.HiddenInput()
#    def clean_content(self):
#        data =  self.cleaned_data['content']
#        if len(data) > 500:
#            raise forms.ValidationError("Comment short be shorter")
#        return data
class CommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
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
