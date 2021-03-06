# Generated by Django 2.0 on 2017-12-19 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='键名', max_length=200)),
                ('value', models.CharField(help_text='键名', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='编码', max_length=50)),
                ('name', models.CharField(help_text='名称', max_length=50)),
                ('address', models.CharField(help_text='所在地', max_length=200)),
                ('assistant_manager', models.CharField(help_text='责任人', max_length=50)),
                ('outer_phone', models.CharField(help_text='联系电话', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='from_organize',
        ),
        migrations.RemoveField(
            model_name='device',
            name='hole_count',
        ),
        migrations.RemoveField(
            model_name='device',
            name='supplier_id',
        ),
        migrations.RemoveField(
            model_name='device',
            name='using_man',
        ),
        migrations.AddField(
            model_name='device',
            name='asset_no',
            field=models.CharField(help_text='资产编号', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='remark',
            field=models.CharField(help_text='备注', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='use_status',
            field=models.CharField(default='', help_text='设备状态', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='arrival_date',
            field=models.DateField(help_text='入厂时间'),
        ),
        migrations.AlterField(
            model_name='device',
            name='duty_officer',
            field=models.CharField(help_text='财产权', max_length=200),
        ),
        migrations.AlterField(
            model_name='device',
            name='management_man',
            field=models.ForeignKey(help_text='管理单位', null=True, on_delete=django.db.models.deletion.PROTECT, to='device.Management'),
        ),
        migrations.AlterField(
            model_name='device',
            name='specs',
            field=models.CharField(help_text='规格', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='asset_class',
            field=models.ForeignKey(help_text='资产类别', null=True, on_delete=django.db.models.deletion.PROTECT, to='device.Asset'),
        ),
    ]
