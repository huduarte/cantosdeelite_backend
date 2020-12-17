#-*- coding: utf-8 -*-

from django.apps import AppConfig


class ConfigConfig(AppConfig):
    class Meta:
        app_label = 'config'
        verbose_name = u'Configuração Geral'
        verbose_name_plural = u"Configuraçãos Geral"

    name = 'config'
    
