# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
#============
import random

#================================================================================

AGE_FROM = 1
AGE_TO = 100

#================================================================================

def my_random_number():
    return random.randint(AGE_FROM, AGE_TO)

class User(AbstractUser):
    """ Custom User class"""
    birthday_date = models.DateField(_("Bithday date"), null=True, blank=True)
    random_number = models.PositiveIntegerField(
                        _("Random number"), 
                        null=True, 
                        blank=True,                         
                        default=my_random_number,
                    )

    def get_absolute_url(self):
        return reverse('users-list')

#================================================================================
