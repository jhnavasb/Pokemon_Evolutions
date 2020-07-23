from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from evolution import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^(?P<pk>[-\w]+)/$', views.PokemonViewSet.as_view())
]
