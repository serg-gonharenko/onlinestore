from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout, forms
from django.contrib.auth.models import User
from users.forms import LoginModelForm, RegisterModelForm, ProfileEditModelForm
from users.models import UserModel


def user_profile_view(request: HttpRequest) -> HttpResponse:
    """User profile view"""
    if request.user.is_authenticated:
        return render(request, "user_profile.html")
    return HttpResponseRedirect(reverse_lazy("login"))


def user_profile_edit_view(request: HttpRequest) -> HttpResponse:
    try:
        instance = UserModel.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ProfileEditModelForm(instance=instance, data=request.POST)
            if form.is_valid():
                form.save()
                # form.save(request.user)
                return HttpResponseRedirect(reverse_lazy("user_profile"))
    else:
        form = ProfileEditModelForm(instance=instance)

    return render(request, "user_profile_edit.html", {'form': form})

    # return render(request, "user_profile_edit.html", {'form': form})
    #     return HttpResponseRedirect(reverse_lazy("user_login"))
    # return HttpResponseRedirect(reverse_lazy("homepage"))


def login_view(request: HttpRequest) -> HttpResponse:
    """Login user view"""
    if request.method == "POST":
        form = LoginModelForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse_lazy("homepage"))
    else:
        form = LoginModelForm()
    return render(request, "user_login.html", {'form': form})


def register_view(request: HttpRequest) -> HttpResponse:
    """ Register new user view """
    if request.method == "POST":
        # form = forms.UserCreationForm()
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.create_user()
            redirect_url = reverse("login")
            return HttpResponseRedirect(redirect_url)
    else:
        form = RegisterModelForm()
    return render(request, "user_register.html", {'form': form})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse_lazy("homepage"))
