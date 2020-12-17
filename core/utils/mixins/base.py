# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext_lazy as _

class BaseMixin(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="data de cadastro no Sistema", auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, verbose_name="data de atualização no Sistema", auto_now=True)

    