from django import forms

from employee_register.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
       model = Employee
       fields = ('nom','prenom','CIN','adresse','telephone','Username','salaire','grade')
       labels = {
           'nom':'Nom',
           'prenom':'Prenom',
           'Username':'Username',
           'CIN':'CIN'
       }

       def __init(self, *args, **kwargs):
           super(EmployeeForm,self).__init__(*args, **kwargs)
           self.fields['position'].empty_label = "Select"
