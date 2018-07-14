# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import UserLogin, MachineRegistration, ComponentRegistration, Assignment, MachineData


admin.site.register(UserLogin)  # This will register my models to admin
# Note: To enable list_display I have to register admin-name too
admin.site.register(MachineRegistration)
admin.site.register(ComponentRegistration)
admin.site.register(Assignment)
admin.site.register(MachineData)
