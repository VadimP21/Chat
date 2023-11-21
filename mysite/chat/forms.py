from django import forms


class IndexForm(forms.Form):
    room_name = forms.CharField(max_length=40)
    nick_name = forms.CharField(max_length=40)
