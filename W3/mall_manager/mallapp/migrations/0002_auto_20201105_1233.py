# Generated by Django 3.1.2 on 2020-11-05 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mallapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stores/'),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='username',
            field=models.CharField(error_messages={'blank': 'شاملو نمیخونیا. شایدم توجه بهم نمیکنی!', 'null': 'شاملو نمیخونیا. شایدم توجه بهم نمیکنی!'}, help_text='نامت را به من بگو', max_length=100, unique=True, verbose_name='نام کاربری'),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mallapp.category'),
        ),
        migrations.AlterField(
            model_name='store',
            name='mall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mallapp.mall'),
        ),
    ]
