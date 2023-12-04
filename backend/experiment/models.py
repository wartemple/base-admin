from django.db import models
from enum import Enum
from model.models import LlmModel

class Experiment(models.Model):
    title = models.CharField(verbose_name="实验名称", max_length=50)
    basic_model = models.ForeignKey(LlmModel, verbose_name="基底模型", on_delete=models.CASCADE)
    output_path = models.CharField(verbose_name="模型输出地址", max_length=50, default='')
    devices = models.CharField(verbose_name="使用设备", max_length=50)

    class Status(Enum):
        CREATED = 'created'           # 创建完成
        CONFIGURED = 'configured'     # 配置完成
        QUEUED = 'queued'             # 排队中
        PENDING = 'pending'           # 创建训练中
        TRAINING = 'training'         # 训练中
        TERMINATED = 'terminated'     # 已终止
        FAILED = 'failed'             # 失败
        SUCCESS = 'success'           # 训练成功

        @classmethod
        def choices(cls):
            return [(e.value, e.name) for e in cls]

    status = models.CharField(verbose_name="实验状态", max_length=50, choices=Status.choices(), default=Status.CREATED.value,)
    config_json = models.JSONField(verbose_name="实验配置json", blank=True)

    class TrainingWays(Enum):
        LORA = 'lora'
        QLORA = 'qlora'
        P_TUNING_V1 = 'p-tuning-v1'
        P_TUNING_V2 = 'p-tuning-v2'

        @classmethod
        def choices(cls):
            return [(e.value, e.name) for e in cls]

    training_way = models.CharField(verbose_name="训练类型", max_length=50, choices=TrainingWays.choices())
    

    def __str__(self):
        return self.name



class ConfigTemplate(models.Model):

    name = models.CharField(verbose_name="配置模板名称", max_length=50)
    

    def __str__(self):
        return self.name


# Create your models here.
class ConfigItem(models.Model):

    class Category(Enum):
        STRING = 'string'
        INTEGER = 'integer'
        FLOAT = 'float'

        @classmethod
        def choices(cls):
            return [(e.value, e.name) for e in cls]

    name = models.CharField(verbose_name="配置项名称", max_length=50)
    key = models.CharField(verbose_name="配置项key", max_length=50)
    default = models.TextField(verbose_name="配置项默认值")
    group = models.CharField(verbose_name="配置项组名称", max_length=50)
    category = models.CharField(verbose_name="配置项类型", max_length=50, choices=Category.choices(), default=Category.STRING.value,)
    meta = models.JSONField(verbose_name="配置项元设置", blank=True)
    template = models.ForeignKey(ConfigTemplate, verbose_name="所属模板", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


