from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['post_type', 'title', 'b_type', 'body', 'region']
        body = forms.CharField( widget=forms.Textarea )
        help_texts = {
            'post_type': None,
            'title': None,
            'b_type': None,
            'body': None,
            'region': None,
        }

        widgets = {
            # 'post_type' : forms.TextInput(attrs={'placeholder': 'CATEGORY'}),
            # 'b_type' : forms.TextInput(attrs={'placeholder': 'BLOODTYPE'}),
            # 'region' : forms.TextInput(attrs={'placeholder': 'REGION'}),
            'title' : forms.TextInput(attrs={'placeholder': 'TITLE'}),
            'body' : forms.TextInput(attrs={'placeholder': 'CONTEXT'}),

        }

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username','email','password','nickname','phone_number','profile_image']
#         help_texts = {
#             'username': None,
#         }

#         widgets = {
#                 'username': forms.TextInput(attrs={'placeholder': 'ID'}),
#                 'password': forms.TextInput(attrs={'placeholder': 'PASSWORD'}),
#                 'email': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
#                 'nickname': forms.TextInput(attrs={'placeholder': 'NICKNAME'}),
#                 'phone_number': forms.TextInput(attrs={'placeholder': 'PHONE NUMBER'}),
#                 'profile_image': forms.TextInput(attrs={'placeholder': 'PROFILE IMAGE'}),   
#             }
