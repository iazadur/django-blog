from django import forms
from App_Blog.models import Blog, Comment


class CreateBlogPost(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_content', 'blog_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)