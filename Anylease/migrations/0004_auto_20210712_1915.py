# Generated by Django 3.2.5 on 2021-07-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anylease', '0003_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='Item_Amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='Item_Category',
            field=models.CharField(choices=[('Electrical Equipments', 'Electrical Equipments'), ('Music Equipments', 'Music Equipments'), ('Electronic Equipments', 'Electronic Equipments'), ('Sports Equipments', 'Sports Equipments'), ('Building/Construction Equipments', 'Building/Construction Equipments'), ('IT Equipments', 'IT Equipments'), ('Audio/Visual Equipments', 'Audio/Visual Equipments'), ('Event Equipments', 'Event Equipments')], default='green', max_length=32),
        ),
    ]