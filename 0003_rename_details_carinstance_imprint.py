from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0002_auto_20210822_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carinstance',
            old_name='details',
            new_name='imprint',
        ),
    ]