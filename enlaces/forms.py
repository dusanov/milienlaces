from django import forms

class FilterForm(forms.Form):
    category = forms.TypedMultipleChoiceField(label='Category', help_text="Select one or more category")
    status = forms.TypedChoiceField(label='Status', help_text="Select status")
    link_type = forms.TypedChoiceField(label='Type', help_text="Select type")
    client = forms.TypedMultipleChoiceField(label='Client', help_text="Select one or more client")
    date_from = forms.DateField(label='From', help_text='Select from date')
    date_to = forms.DateField(label='To', help_text='Select to date')
    
