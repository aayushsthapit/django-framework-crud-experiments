# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import ModelViewSet
from models import FixedDataTable
from serializer import FixedDataTableSerializer

from django.shortcuts import render

class ListTableData(ModelViewSet):
    queryset=FixedDataTable.objects.all()
    serializer_class = FixedDataTableSerializer
