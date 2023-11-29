from django.db import models

# Create your models here.
class LlmModel(models.Model):
    name = models.CharField(_("模型名称"), max_length=50)
    tags = models.CharField(_("模型标签"), max_length=50)
    path = models.CharField(_("模型地址"), max_length=100)
    publisher = models.CharField(_("模型发布者"), max_length=50)
    introduce = models.TextField(_("模型介绍"))

    class Meta:
        verbose_name = _("LlmModel")
        verbose_name_plural = _("LlmModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LlmModel_detail", kwargs={"pk": self.pk})
