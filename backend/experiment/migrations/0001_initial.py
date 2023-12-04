# Generated by Django 4.1.3 on 2023-11-29 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='配置模板名称')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='实验名称')),
                ('output_path', models.CharField(default='', max_length=50, verbose_name='模型输出地址')),
                ('devices', models.CharField(max_length=50, verbose_name='使用设备')),
                ('status', models.CharField(choices=[('created', 'CREATED'), ('configured', 'CONFIGURED'), ('queued', 'QUEUED'), ('pending', 'PENDING'), ('training', 'TRAINING'), ('terminated', 'TERMINATED'), ('failed', 'FAILED'), ('success', 'SUCCESS')], default='created', max_length=50, verbose_name='实验状态')),
                ('config_json', models.JSONField(blank=True, verbose_name='实验配置json')),
                ('training_way', models.CharField(choices=[('lora', 'LORA'), ('qlora', 'QLORA'), ('p-tuning-v1', 'P_TUNING_V1'), ('p-tuning-v2', 'P_TUNING_V2')], max_length=50, verbose_name='训练类型')),
                ('basic_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.llmmodel', verbose_name='基底模型')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('string', 'STRING'), ('integer', 'INTEGER'), ('float', 'FLOAT')], default='string', max_length=50, verbose_name='配置项类型')),
                ('name', models.CharField(max_length=50, verbose_name='配置项名称')),
                ('key', models.CharField(max_length=50, verbose_name='配置项key')),
                ('default', models.TextField(verbose_name='配置项默认值')),
                ('group', models.CharField(max_length=50, verbose_name='配置项组名称')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiment.configtemplate', verbose_name='所属模板')),
            ],
        ),
    ]
