from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import UsuarioCreate, UsuarioList, UsuarioUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cambiar-clave/', login_required(auth_views.PasswordChangeView.as_view(template_name='password_change_form.html')), name='password_change'),
    path('cambiar-clave-hecho/', login_required(auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')), name='password_change_done'),

    path('', login_required(UsuarioList.as_view()), name='usuario_lista'),
    path('registro/', login_required(UsuarioCreate.as_view()), name='usuario_registro'),
    path('actualizar/<int:pk>/', login_required(UsuarioUpdate.as_view()), name='usuario_actualizar'),
    #path('eliminar/<int:pk>/', login_required(UsuarioDelete.as_view()), name='usuario_eliminar'),
]
