#-*- coding: utf-8 -*-
from django.db import models

from core.utils.mixins.base import BaseMixin

DEFAULT_FEVER = 38

class Config(BaseMixin):
    class Meta:
        verbose_name = u'Configuração Geral'
        verbose_name_plural = u"Configuraçãos Geral"

    name = models.CharField(max_length=50)
    endpoint = models.CharField(max_length=200, unique=True)
    token = models.CharField(max_length=200, null=True, blank=True)
    logo_url = models.CharField(max_length=200, null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)
    terms = models.TextField(null=True, blank=True)
    lgpd_terms = models.TextField(null=True, blank=True)
    febre_number = models.FloatField(default=38)

    def __str__(self):
        return self.endpoint

    @staticmethod
    def get_config():
        return Config.objects.filter(is_active=True).first()