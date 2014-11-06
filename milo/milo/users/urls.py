from django.conf.urls import url
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from milo.users.models import User

urlpatterns = [
    url(r'^$', ListView.as_view(
            queryset=User.objects.order_by('-id'),
            context_object_name='users_list',
            template_name='users/users_list.html'),
            name='users-list'),
    url(r'^create/$', CreateView.as_view(
            model=User,
            template_name_suffix='_create_form',
            fields=['username','password','birthday_date','random_number']),
            name='user-create'),
    url(r'^edit/(?P<pk>[^/]+)/$', UpdateView.as_view(
            model=User,
            template_name_suffix='_edit_form',
            fields=['username','password','birthday_date','random_number']),
            name='user-edit'),
    url(r'^delete/(?P<pk>[^/]+)/$', DeleteView.as_view(
            model=User,
            template_name_suffix='_delete_form',
            success_url='/'),
            name='user-delete'),
    url(r'^csv_export/$', 'milo.users.views.export_csv',name='csv-list'),
]

