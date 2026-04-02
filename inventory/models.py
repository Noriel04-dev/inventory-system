from django.db import models

CATEGORY_CHOICES = [
    ('Desktop', 'Desktop'),
    ('Laptop', 'Laptop'),
    ('Printer', 'Printer'),
    ('Security', 'Security'),
    ('Network Devices', 'Network Devices'),
    ('Electrical Devices', 'Electrical Devices'),
    ('Tools', 'Tools'),
    ('Telephony', 'Telephony'),
    ('Display', 'Display'),
]

CLASSIFICATION_CHOICES = [
    ('Components', 'Components'),
    ('Parts', 'Parts'),
]

STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Under Repair', 'Under Repair'),
    ('Disposed', 'Disposed'),
    ('For Repair', 'For Repair'),
]


class InventoryItem(models.Model):
    id_number = models.CharField(max_length=100, blank=True)
    asset_tag = models.CharField(max_length=100, blank=True)
    computer_tag = models.CharField(max_length=100, blank=True)
    display_tag = models.CharField(max_length=100, blank=True)
    brand = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    work_order = models.CharField(max_length=100, blank=True)
    inventory_receipt = models.CharField(max_length=100, blank=True)
    inventory_issuance = models.CharField(max_length=100, blank=True)
    po = models.CharField(max_length=100, blank=True, verbose_name='PO')
    remarks = models.TextField(blank=True)
    assigned_person = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    project_site = models.CharField(max_length=200, blank=True)
    serial_number = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')
    reference_number = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES)
    import_batch = models.CharField(max_length=100, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id_number} - {self.brand} {self.model}"

    class Meta:
        ordering = ['-created_at']
