from django.urls import path
from . import views
urlpatterns = [
    path('',views.listview.as_view(),name='listview'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detailview'),
]
