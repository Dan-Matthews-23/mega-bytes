
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .webhooks import webhook


urlpatterns = [
    #path('', views.showOrders, name='showOrders'),
    path('', views.profile, name='profile'),
    path('order_history/',
         views.order_history,
         name='order_history'),
    
    


] 


