

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=256, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст объявления')),
                ('category', models.CharField(choices=[('TNK', 'Танки'), ('HLS', 'Хилы'), ('DMG', 'ДД'), ('TRD', 'Торговцы'), ('GMS', 'Гилдмастеры'), ('QST', 'Квестгиверы'), ('SMT', 'Кузнецы'), ('LTH', 'Кожевники'), ('PTN', 'Зельевары'), ('SPL', 'Мастера заклинаний')], max_length=3, verbose_name='Категория')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст сообщения')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.advert', verbose_name='Отклик')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
            },
        ),
    ]
