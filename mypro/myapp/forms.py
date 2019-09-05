
from django import forms
from .models import Register


class regform(forms.ModelForm):
    class Meta:
        model=Register
        fields = "__all__"


class logform(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(max_length=20)  



class InsertingDataForm(forms.Form):
    id = forms.IntegerField(
        label='Employee ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Employee Id'
            }
        )
    )
    name = forms.CharField(
        label= 'Employee Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Employee Name'
            }
        )
    )
    role = forms.CharField(
        label= 'Employee role',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Employee role'
            }
        )
    )
  

class UpdateDataForm(forms.Form):
    id = forms.IntegerField(
        label='Employee ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Id'
            }
        )
    )


    name = forms.CharField(
        label= 'Employee Name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Employee Name'
            }
        )
    )

    role = forms.CharField(
        label='Employee role',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee role'
            }
        )
    )




class DeleteDataForm(forms.Form):
    id = forms.IntegerField(
        label='Employee ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Employee Id'
            }
        )
    )
