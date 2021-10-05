from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0003_rename_details_carinstance_imprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='car_image'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='car_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='car_image'),
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(help_text='Please enter your full name (e.g. David, Kamau...)', max_length=200, verbose_name='owner_name')),
                ('owner_IDno', models.CharField(help_text='Please enter your ID number (e.g. 12345678...)', max_length=8, unique=True, verbose_name='owner_IDno')),
                ('owner_email', models.CharField(help_text='Please enter your email (e.g. david@gmail.com)', max_length=200, verbose_name='owner_email')),
                ('car_image', models.ImageField(null=True, upload_to='images/', verbose_name='car_image')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='carlisting.car')),
            ],
        ),
    ]