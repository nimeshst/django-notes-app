"""myproject URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from notes.views import home
from notes.views import notes_title
from notes import views
from notes.views import user_note
from notes.views import display_note
from notes.views import delete_note
# url(regex, view, kwargs, name)
from accounts import views as acc_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),
    url(r'^user_note/', user_note, name='user_note'),

    # valid url /notes/1/
    # captures {'pk':1}
    url(r'^notes/(?P<pk>\d+)/$', notes_title, name='notes_title'),

    # url for the new topic
    url(r'^new_note/$', views.NewNoteView.as_view(), name='new_note'),
    #as_view() returns the view function of the url patterns

    url(r'^delete_note/(?P<pk>\d+)/$', delete_note, name='delete_note'),

    url(r'^display_note/(?P<pk>\d+)/$', display_note, name='display_note'),

    url(r'^edit_note/(?P<pk>\d+)/$', views.edit_note, name='edit_note'),

    url(r'^signup/$', acc_views.signup, name='signup'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'login.html'),
         name='login'),
]
