from django import forms 

class Search(forms.Form):
	search_text = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Search term..",'class':'form-control',"name":"x"}))