from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventoryitem_project_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='import_batch',
            field=models.CharField(blank=True, db_index=True, max_length=100),
        ),
    ]
