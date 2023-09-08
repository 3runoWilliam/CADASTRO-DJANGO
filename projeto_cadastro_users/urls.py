from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listagem', views.listagem, name='listagem_users'),
    path('usuarios/', views.listagem_users, name='listagem_users'),
    # path('admin/', admin.site.urls),
]
