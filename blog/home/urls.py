from django.urls import path
from home.views import IndexView, DetailView, SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
]
