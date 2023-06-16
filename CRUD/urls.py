from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('',views.index),
    path('create', views.create),
    path('retrieve', views.retrieve, name="retrieve"),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.updateData),
    # url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete),  
    path('delete/<int:id>',views.delete),
]
