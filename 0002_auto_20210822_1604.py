from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='carlisting.carmake'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='carlisting.carmodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='carlisting.cartype'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(help_text='Some additional info about the car', max_length=1000),
        ),
        migrations.AlterField(
            model_name='car',
            name='registration',
            field=models.CharField(max_length=7, unique=True, verbose_name='Reg No.'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carmake',
            name='car_make',
            field=models.CharField(help_text='Please enter car make (e.g. Toyota, Nissan...)', max_length=200, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_model',
            field=models.CharField(help_text='Please enter car model (e.g. Corolla, Sunny...)', max_length=200, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='cartype',
            name='car_type',
            field=models.CharField(help_text='Please enter car type (e.g. SUV, Saloon...)', max_length=200),
        ),
    ]