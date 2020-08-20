from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('add_task/', views.addTask, name="add_task"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)