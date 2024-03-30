from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import SearchForm
from .models import News, CategoryModel


def news(request):
    news_title = News.objects.all()
    return render(request, 'index.html', {'news_title': news_title})

class HomePage(ListView):
    form = SearchForm
    template_name = 'index.html'
    model = News
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["news"] = News.objects.all()
        return context

class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    if request.method == "POST":
        get_news = request.POST.get('search_news')
        try:
            exact_news = News.objects.get(title__icontains=get_news)
            return redirect(f'/news/{exact_news.id}')
        except:
            return redirect('/')


def news_page(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_page.html', {'news_item': news_item})
def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_news = News.objects.filter(news_category=category)
    context = {'news': current_news}
    return render(request, 'category.html', context)

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def category(request):
    return render(request, 'category.html')

def clients(request):
    return render(request, 'clients.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')