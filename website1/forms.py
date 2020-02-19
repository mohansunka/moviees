from django import forms
from website1.models import Movie

class MovieForm(forms.ModelForm):
	class Meta:
		model=Movie
		fields='__all__'