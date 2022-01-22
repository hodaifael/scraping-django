from django.conf.urls import url 
from product import views 
from product.views import * 




urlpatterns = [ 
    url('index',view=getproduct, name='getproduct'),
    url('amazon',view=getproductamazon, name='amazon'),
]
