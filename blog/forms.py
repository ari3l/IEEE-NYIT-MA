from django import forms
from .models import Project, User

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'email', 'title', 'description')

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('name', 'year', 'email','graduation', 'alumni')
			
		
