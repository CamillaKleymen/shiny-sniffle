from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from news.views import HomePage, MyLoginView, logout_view, search, news_page, category_page, about, index, clients, contact, allnews, category, news
from news.views import addnews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('login/', MyLoginView.as_view()),
    path('logout/', logout_view),
    path('search', search),
    path('about.html', about, name='about'),
    path('index.html', index, name='home'),
    path('category.html', category, name='category'),
    path('clients.html', clients, name='clients'),
    path('contact.html', contact, name='contact'),
    path('allnews', allnews, name='allnews'),
    path('news_page', news_page, name='news_page'),
    path('news/<int:pk>', news, name='news'),
    path('category/<int:pk>', category_page),
    path('addnews/', addnews, name='add_news'),
    # path('news/detail/', news_detail, name='news_detail'),
]
