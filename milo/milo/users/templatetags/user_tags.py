# coding: utf-8
from django import template
from django.utils.translation import ugettext_lazy as _
from dateutil.relativedelta import relativedelta
from datetime import date

register = template.Library()

@register.simple_tag
def user_allowed(user):
    if user.birthday_date:
        birth_date = date(user.birthday_date.year, user.birthday_date.month, user.birthday_date.day)
        today = date.today()
        difference_in_years = relativedelta(today, birth_date).years
        if difference_in_years > 13:
            return "allowed"
    return "blocked"

@register.simple_tag
def modulo(value):
    if value:
        temp_value = ""
        if value % 3 == 0:
            temp_value += "Bizz"
        if value % 5 == 0:
            temp_value += "Fuzz"
        if temp_value:
            return temp_value
  
    return value
         
