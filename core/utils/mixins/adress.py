# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext_lazy as _
from core.django_google_maps import fields as map_fields

class AdressMixin(models.Model):
    class Meta:
        abstract = True

    address = map_fields.AddressField(max_length=150, verbose_name=u"endereço", blank=True)
    geolocation = map_fields.GeoLocationField(default='-12.9510242,-38.4414401', max_length=60, verbose_name=u"geolocalização", blank=True)
    cidade = models.CharField(max_length=80, blank=True)
    pais = models.CharField(max_length=80, verbose_name=u"país", blank=True)
    estado = models.CharField(max_length=80, blank=True)
    bairro = models.CharField(max_length=80, blank=True, verbose_name="Comunidade")
    complemento = models.CharField(max_length=80, blank=True)
