from django import forms


class RegForm(forms.Form):
    username = forms.RegexField(regex="^[A-Za-z0-9-_]+$", min_length=3, label="Логин", required=True)
    email = forms.EmailField(label="Эл. почта", required=True)
    password1 = forms.RegexField(widget=forms.PasswordInput(), regex="(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}", min_length=6, label='Пароль', required=True)
    password2 = forms.RegexField(widget=forms.PasswordInput(), regex="(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}", min_length=6, label='Повторите пароль', required=True)

class Change_profile(forms.Form):
    first_name = forms.CharField(label='Ваше имя', required=False)
    last_name = forms.CharField(label='Ваша фамилия', required=False)
    password1 = forms.RegexField(widget=forms.PasswordInput(), regex="(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}", min_length=6, label='Новый пароль', required=False)
    password2 = forms.RegexField(widget=forms.PasswordInput(), regex="(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}", min_length=6, label='Повторите пароль', required=False)
