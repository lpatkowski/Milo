from django.shortcuts import render
from django.http import HttpResponse
import csv
from milo.users.models import User
from milo.users.templatetags.user_tags import *

def export_csv(request):
    users = User.objects.all().order_by("-id")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 
                     'Birthday', 
                     'Eligible', 
                     'Random Number',
                     'BizzFuzz',
    ])

    for user in users:
        writer.writerow([user.username, 
                         user.birthday_date or "", 
                         user_allowed(user),
                         str(user.random_number or ""),
                         str(modulo(user.random_number) or ""),      
                       ])
          
    return response
