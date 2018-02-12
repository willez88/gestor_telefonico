from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Perfil
from .forms import UsuarioForm, UsuarioUpdateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class UsuarioList(ListView):
    model = User
    template_name = "usuario.lista.html"

    def get_queryset(self):
        queryset = Perfil.objects.filter(users=self.request.user).exclude(user=self.request.user)
        return queryset

class UsuarioCreate(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = "usuario.registro.html"
    success_url = reverse_lazy('usuario_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.username = form.cleaned_data['cedula']
        self.object.first_name = form.cleaned_data['nombre']
        self.object.last_name = form.cleaned_data['apellido']
        self.object.email = form.cleaned_data['correo']
        self.object.set_password(form.cleaned_data['password'])
        self.object.is_active = True
        self.object.save()

        user = User.objects.get(username=self.request.user.username)
        Perfil.objects.create(
            telefono=form.cleaned_data['telefono'],
            user= self.object,
            users=user
        )
        return super(UsuarioCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(UsuarioCreate, self).form_invalid(form)

class UsuarioUpdate(UpdateView):
    model = User
    form_class = UsuarioUpdateForm
    template_name = "usuario.registro.html"
    success_url = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.kwargs['pk']:
            return super(UsuarioUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('error_403')

    def get_initial(self):
        datos_iniciales = super(UsuarioUpdate, self).get_initial()
        user = User.objects.get(pk=self.object.id)
        datos_iniciales['cedula'] = user.username
        datos_iniciales['nombre'] = user.first_name
        datos_iniciales['apellido'] = user.last_name
        datos_iniciales['correo'] = user.email
        perfil = Perfil.objects.get(user=user)
        datos_iniciales['telefono'] = perfil.telefono
        return datos_iniciales

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.first_name = form.cleaned_data['nombre']
        self.object.last_name = form.cleaned_data['apellido']
        self.object.email = form.cleaned_data['correo']
        self.object.save()

        if Perfil.objects.filter(user=self.object):
            perfil = Perfil.objects.get(user=self.object)
            perfil.telefono = form.cleaned_data['telefono']
            perfil.save()
        return super(UsuarioUpdate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(UsuarioUpdate, self).form_invalid(form)

"""class UsuarioDelete(DeleteView):
    model = User
    template_name = "usuario.eliminar.html"
    success_url = reverse_lazy('usuario_lista')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.kwargs['pk']:
            return super(UsuarioDelete, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('error_403')"""
