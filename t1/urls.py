from django.urls import path

from t1 import views

app_name = 't1'

urlpatterns = [
    path('', views.CharacterListView.as_view(),name='character_list'),
]