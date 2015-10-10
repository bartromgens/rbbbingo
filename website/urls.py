from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import HomeView
from website.views import CardsView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')), # the django-registration module
    url(r'^cards/', CardsView.as_view()),
)
