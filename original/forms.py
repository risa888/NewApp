from django.contrib.auth.forms import AuthenticationForm 


# from original.models import UserDetail


class LoginForm(AuthenticationForm 
):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   

    # class Meta(RegistrationForm.Meta):
    #     model = UserDetail
        