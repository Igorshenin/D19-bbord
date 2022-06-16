

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='text',
        ),
        migrations.AddField(
            model_name='advert',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст объявления'),
        ),
    ]
