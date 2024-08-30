


from django import forms

class UserRegisterForm(forms.Form):
    image = forms.ImageField(required=False)
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    def clear(self):

        cleaned_data = super().clear()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password == confirm_password:
            raise forms.ValidationError("passwords don't match")
        return cleaned_data

class LoginRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
