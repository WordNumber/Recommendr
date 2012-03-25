from django import forms

class BlogForm(forms.Form):
    blog_url = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Blog URL'}))