from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('land-inventory', views.land_inventory, name='land_inventory'),
    path('applicant', views.applicant, name='applicant'),
    path('app_payment', views.app_payment, name='app_payment'),
    path('app_profile', views.app_profile, name='app_profile'),
    path('app_status', views.app_status, name='app_status'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('drone', views.drone, name='drone'),
    path('implementing_home', views.implementing_home, name='implementing_home'),
    path('nodal', views.nodal, name='nodal'),

    path('app_apply', views.app_apply, name='app_apply'),
    path('imp_apply', views.imp_apply, name='imp_apply'),
    path('imp_profile', views.imp_profile, name='imp_profile'),

    path('imp_transaction', views.imp_transaction, name='imp_transaction'),
    path('nod_drone', views.nod_drone, name='nod_drone'),
    path('documentation', views.documentation, name='documentation'),
    path('earn', views.earn, name='earn'),
    path('ind', views.ind, name='ind')



]
