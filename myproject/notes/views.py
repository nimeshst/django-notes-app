# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import TextNotes
from .forms import NewNoteForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    # home page of the site
    return render(request, 'home.html')


def notes_title(request, pk):
    note_title = TextNotes.objects.get(pk=pk)
    return render(request, 'notetitle.html', {'note_title': note_title})


@method_decorator(login_required, name='dispatch')
class NewNoteView(View):
    # login required for creating the new note

    def post(self, request):
        # if form is submitted
        # create form instance
        form = NewNoteForm(request.POST)
        if form.is_valid():
            # get the user
            TextNotes.objects.create(
                title = form.cleaned_data.get('title'),
                note = form.cleaned_data.get('note'),
                created_by = request.user)
            return redirect('user_note')
        return render(request, 'new_note.html', {'form': form})

    def get(self, request):
        # render the form with its normal fields
        form = NewNoteForm()

        return render(request, 'new_note.html', {'form': form})


@login_required
def user_note(request):
    # display the logged in user's notes
    # get all the notes created by the user

    user_text_note = TextNotes.objects.filter(created_by=request.user).order_by('-updated_at')
    username = request.user.username
    return render(request, 'user_note.html',
                  {'user_text_note': user_text_note,
                   'username': username,
                   })


@login_required
def display_note(request, pk):
    # diplay user notes in new page
    # return HttpResponse("hello world")
    user_note = TextNotes.objects.get(pk=pk)
    return render(request, 'display_note.html', {'user_note': user_note})


@login_required
def delete_note(request, pk):

    TextNotes.objects.filter(pk=pk).delete()
    return redirect('user_note')

# edit view
@login_required
def edit_note(request, pk):
    note = TextNotes.objects.get(pk=pk)
    if request.method == "POST":
        form = NewNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.updated_at = timezone.now()
            print(note.updated_at)
            # just realize that this field is completly useless
            note.updated_by = request.user
            note.save()
            return redirect('user_note')
        else:
            form = NewNoteForm(instance=note)
    else:
        form = NewNoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})
