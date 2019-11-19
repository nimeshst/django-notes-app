# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login
# Create your views here.
from .forms import SignUpForm
from django.shortcuts import render
from django.shortcuts import redirect


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_note')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
