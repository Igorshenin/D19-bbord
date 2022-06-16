

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_remove_advert_text_advert_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст объявления'),
        ),
    ]
