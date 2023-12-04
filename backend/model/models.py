from django.db import models

# Create your models here.
class LlmModel(models.Model):
    name = models.CharField(verbose_name="模型名称", max_length=50)
    tags = models.CharField(verbose_name="模型标签", max_length=50)
    path = models.CharField(verbose_name="模型地址", max_length=100)
    publisher = models.CharField(verbose_name="模型发布者", max_length=50)
    introduce = models.TextField(verbose_name="模型介绍")


    def __str__(self):
        return self.name
