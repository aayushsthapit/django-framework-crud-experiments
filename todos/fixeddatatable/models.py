# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FixedDataTable(models.Model):
    name=models.CharField(max_length=200);
    category=models.CharField(max_length=200);
    created_at=models.DateTimeField(auto_now_add=True)
