#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import ListView
from milo.users.models import User

#======================================================================================

class CustomUsersListView(ListView):
    model = User

#======================================================================================

