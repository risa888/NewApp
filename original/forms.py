from django_registration.forms import RegistrationForm
from original.models import UserDetail


class LoginForm(RegistrationForm):
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'
    #         field.widget.attrs['placeholder'] = field.label   

    class Meta(RegistrationForm.Meta):
        model = UserDetail
        fields = ['username', 'email', 'password']