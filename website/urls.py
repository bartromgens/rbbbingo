from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from registration.forms import RegistrationFormUniqueEmail
from registration.views import RegistrationView

from website.views import CardsView
from website.views import CheckFieldView
from website.views import EventsView
from website.views import GamesView
from website.views import HomeView
from website.views import JoinGameView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'), # include before the simple.urls to override register url
    url(r'^accounts/', include('registration.backends.simple.urls')), # the django-registration module
    url(r'^cards/', login_required(CardsView.as_view())),
    url(r'^games/', login_required(GamesView.as_view())),
    url(r'^events/', login_required(EventsView.as_view())),
    url(r'^field/toggle/(?P<field_id>[0-9]+)/$', login_required(CheckFieldView.as_view())),
    url(r'^game/join/(?P<game_id>[0-9]+)/$', login_required(JoinGameView.as_view())),
)
