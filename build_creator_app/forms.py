from django import forms

class ResourceForm(forms.Form):
    wood = forms.IntegerField(label="Wood", min_value=0, required=True)
    food = forms.IntegerField(label="Food", min_value=0, required=True)
    gold = forms.IntegerField(label="Gold", min_value=0, required=True)
    stone = forms.IntegerField(label="Stone", min_value=0, required=True)
