from django.urls import path
from . import views

app_name="movies"

urlpatterns=[
    path('index/', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    path('<int:movies_pk>detail/', views.detail, name="detail"),
    path('<int:movies_pk>/delete/', views.delete, name="delete"),
    path('<int:movies_pk>/edit/', views.edit, name="edit"),
    path('<int:movies_pk>/update/', views.update, name="update")
]