from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect


def logout_view(request):
    logout(request)
    return redirect("/")