from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('anime/', views.anime, name='anime'),

]