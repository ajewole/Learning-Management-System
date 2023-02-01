from django import forms
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


    
class NewCourseForm(forms.ModelForm):    
    class Meta:
        model = Course
        fields =['title','duration' ,'description','course_fee','resources','learning_outcomes','course_image']
    
class CreateUserForm(UserCreationForm):
    email=forms.CharField(required=True,max_length=254,
    widget=forms.EmailInput(),help_text='Enter a valid Email address')
    class Meta:
        model = User
        fields = [ 'username','email','password1','password2']


