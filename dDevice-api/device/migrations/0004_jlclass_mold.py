# Generated by Django 2.0 on 2017-12-21 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20171219_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='JlClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='键名', max_length=200)),
                ('value', models.CharField(help_text='键名', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.CharField(help_text='二维码', max_length=200)),
                ('code', models.CharField(help_text='编码', max_length=50)),
                ('arrival_date', models.DateField(help_text='入厂时间')),
                ('specs', models.CharField(help_text='规格', max_length=200, null=True)),
                ('hole_count', models.CharField(help_text='穴数', max_length=200, null=True)),
                ('duty_officer', models.CharField(help_text='财产权', max_length=200)),
                ('jl_dosage', models.CharField(default='', help_text='胶料用量', max_length=200)),
                ('use_status', models.CharField(choices=[('lh', '良好'), ('jc', '较差'), ('gz', '故障'), ('jx', '检修')], default='lh', help_text='使用状态', max_length=20)),
                ('location', models.CharField(default='', help_text='位置', max_length=200)),
                ('price', models.CharField(help_text='价格', max_length=200)),
                ('remark', models.CharField(help_text='备注', max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('asset_class', models.ForeignKey(help_text='资产类别', null=True, on_delete=django.db.models.deletion.PROTECT, to='device.Asset')),
                ('jl_class', models.ForeignKey(help_text='胶料类型', null=True, on_delete=django.db.models.deletion.PROTECT, to='device.JlClass')),
                ('management_man', models.ForeignKey(help_text='管理单位', null=True, on_delete=django.db.models.deletion.PROTECT, to='device.Management')),
            ],
        ),
    ]