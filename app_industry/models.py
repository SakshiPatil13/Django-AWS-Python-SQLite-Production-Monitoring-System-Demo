# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserLogin(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.username)

    class Meta:   # To Display the name in Admin Panel
        # Model name correction; it appears login(extra s) in Admin Panel
        verbose_name_plural = "Login"
        # Model name correction; it appears login(extra s) in Admin Panel


# Creating a machine_registration table in django database to see in
# Django Administration
class MachineRegistration(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    user_info = models.ForeignKey("UserLogin", null=False)
    # user_info from the user_login table will be chosen as player from drop
    # down
    machine_number = models.CharField(max_length=255, null=True)
    machine_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.machine_number)

    class Meta:   # To Display the name in Admin Panel
        # Model name correction; it appears login(extra s) in Admin Panel
        verbose_name_plural = "Machine Registration"

 # Creating a component_registration table in django database to see in
 # Django Administration


class ComponentRegistration(models.Model):
     # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    component_number = models.CharField(max_length=255, null=True)
    component_description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.component_number)

    class Meta:   # To Display the name in Admin Panel
        # Model name correction; it appears login(extra s) in Admin Panel
        verbose_name_plural = "Component Registration"

 # Creating a component_assignment table in django database to see in
 # Django Administration


class Assignment(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    machine_number = models.ForeignKey("MachineRegistration", null=False)

    component_number = models.ForeignKey("ComponentRegistration", null=False)

    def __str__(self):
        return str(self.machine_number)

    class Meta:
        verbose_name_plural = "Assignment"


# Creating a machine_data table in django database to see in Django
# Administration
class MachineData(models.Model):

    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    machine_number = models.CharField(max_length=255, null=True)
    component_number = models.ForeignKey("ComponentRegistration", null=False)
    # Component from the component_assignment table will be chosen as player
    # from drop down
    status = models.CharField(max_length=255, null=True)
    pieces = models.IntegerField(default=0)
    cycle_time = models.IntegerField(default=0)
    running_time = models.IntegerField(default=0)
    downtime = models.IntegerField(default=0)
    stops = models.IntegerField(default=0)

    def __str__(self):
        return str(self.machine_number)

    class Meta:   # To Display the name in Admin Panel
        # Model name correction; it appears login(extra s) in Admin Panel
        verbose_name_plural = "Machine Data"
