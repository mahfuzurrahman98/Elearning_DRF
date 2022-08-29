
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.CRUD.as_view()),
    path('student/<int:id>/', views.CRUD.as_view()),
]
