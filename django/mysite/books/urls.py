from django.conf.urls import url, include
from django.views.generic import DetailView, ListView
from .models import Book
from . import views


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    slug_field = 'name'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book_list'

urlpatterns = [
    url(r'^show_header/$', views.show_header),
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks),
    url(r'^detail/(?P<slug>.*?)/$', BookDetailView.as_view()),
    #url(r'^detail/(?P<pk>[0-9]+)/$', BookDetailView.as_view()), 
    url(r'^list/$', BookListView.as_view())
]