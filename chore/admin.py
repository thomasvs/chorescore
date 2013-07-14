# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

from django.contrib import admin
from chore import models

admin.site.register(models.Chore)
admin.site.register(models.Period)
admin.site.register(models.Score)
