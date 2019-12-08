from django import forms


class DummyForm1(forms.Form):
    title = forms.CharField(label='title', min_length=1, max_length=64)
    description = forms.CharField(label='description', min_length=1, max_length=1024)
    price = forms.IntegerField(label='price', min_value=1, max_value=1000000)


class DummyForm2(forms.Form):
    text = forms.CharField(label='text', min_length=1, max_length=1024)
    grade = forms.IntegerField(label='grade', min_value=1, max_value=10)


