from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add_item',views.add_todo,name='add_todo'),
    path('deletetodo/<int:pk>',views.delete_todo,name='delete_todo'),
]