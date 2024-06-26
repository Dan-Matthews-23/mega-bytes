
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [

    path('render_profile', views.render_profile, name='render_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('order_history/<order_number>/rate',
         views.leave_review,
         name='leave_review'),
]
