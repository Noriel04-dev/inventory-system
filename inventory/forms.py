from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    purchase_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
    )

    class Meta:
        model = InventoryItem
        fields = [
            'id_number', 'asset_tag', 'computer_tag', 'display_tag',
            'brand', 'model', 'work_order', 'inventory_receipt',
            'inventory_issuance', 'po', 'remarks', 'assigned_person',
            'department', 'project_site', 'serial_number', 'type', 'status',
            'reference_number', 'purchase_date', 'category', 'classification'
        ]
        widgets = {f: forms.TextInput(attrs={'class': 'form-control form-control-sm'}) for f in [
            'id_number', 'asset_tag', 'computer_tag', 'display_tag',
            'brand', 'model', 'work_order', 'inventory_receipt',
            'inventory_issuance', 'po', 'assigned_person', 'department',
            'project_site', 'serial_number', 'type', 'reference_number'
        ]}
        widgets['remarks'] = forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2})
        widgets['status'] = forms.Select(attrs={'class': 'form-select form-select-sm'})
        widgets['category'] = forms.Select(attrs={'class': 'form-select form-select-sm'})
        widgets['classification'] = forms.Select(attrs={'class': 'form-select form-select-sm'})
        widgets['purchase_date'] = forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-sm'})
