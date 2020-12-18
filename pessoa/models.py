import uuid

from datetime import datetime, timedelta

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from django.db import models
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.db.models import F

from core.utils.mixins.base import BaseMixin

User = get_user_model()

class Pessoa(BaseMixin):
    class Meta:
        verbose_name = u'Pessoa' 
        verbose_name_plural = u'Pessoas'
        ordering = ['-created_at']

    uuid = models.UUIDField(unique=True, default= uuid.uuid4)
    email = models.EmailField(_('email address'), null=True, blank=True)
    name = models.CharField(max_length=100, blank=True ,null=True,verbose_name='Name', default='')

    def __str__(self):
        return "{}".format(
            self.name if self.name else u'Não Fornecido',
        )