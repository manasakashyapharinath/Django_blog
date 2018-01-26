from django import forms 

class UserForm(forms.Form):
 userName = forms.CharField(required = True, label = 'userName', max_length = 32)
 password = forms.CharField( required = True, label = 'password',max_length = 32)

class blogForm(forms.Form):

 #author = forms.CharField(label='comment', max_length = 32,required = True)
 title = forms.CharField(label='comment', max_length = 32,required = True)
 text= forms.CharField(label='comment', max_length = 3200,required = True,widget=forms.Textarea)
