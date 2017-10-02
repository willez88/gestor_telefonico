from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import UsuarioCreate, UsuarioList, UsuarioUpdate, UsuarioDelete

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^cambiar-clave/$', login_required(auth_views.PasswordChangeView.as_view(template_name='password_change_form.html')), name='password_change'),
    url(r'^cambiar-clave-hecho/$', login_required(auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')), name='password_change_done'),

    url(r'^$', login_required(UsuarioList.as_view()), name='usuario_lista'),
    url(r'^registro/$', login_required(UsuarioCreate.as_view()), name='usuario_registro'),
    url(r'^actualizar/(?P<pk>\d+)/$', login_required(UsuarioUpdate.as_view()), name='usuario_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(UsuarioDelete.as_view()), name='usuario_eliminar'),
]
