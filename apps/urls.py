from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_list_view),
    path('<int:pk>/', views.user_detail_view),
    path('<int:pk>/update/', views.user_update_view),
    path('<int:pk>/delete/', views.user_delete_view)
]
