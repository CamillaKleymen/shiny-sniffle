from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import NewsForm
from .models import News, CategoryModel


def news(request):
    news_title = News.objects.all()
    print(news_title)
    print('asfsdf')

    return render(request, 'news_page.html', {'news_title': news_title}, )


class HomePage(ListView):
    model = News
    template_name = 'index.html'

    def newsform(self, request):
        form = NewsForm()
        return render(request, 'news_page.html', {'form': form})
        # form = NewsForm
        # template_name = 'index.html'
        # model = News
        # paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["news"] = News.objects.all()
        return context

    def news_list(request):
        news_items = News.objects.all().order_by('-published_date')[:3]
        return render(request, 'news_page.html', {'news_items': news_items})


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


def news_page(request):
    news_list = News.objects.all()
    return render(request, 'news_page.html', {'news_list': news_list})


# def addnews():
#         class
#         form = NewsForm(request.POST)
#         news = News.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.news = news
#             form.save()
#             # form.news_id = pk
#         return redirect('/')


def category_page(request, pk):
    category = CategoryModel.objects.all(id=pk)
    current_news = News.objects.filter(news_category=category)
    context = {'news': current_news}
    return render(request, 'category.html', context)


# def news_detail(request, pk):
#     news_item = News.objects.all(pk=pk)
#     current_news = News.objects.filter(news_category=category)
#     context = {'news': current_news}
#     return render(request, 'news_detail.html', {'news_item': news_item}, context)
def addnews(request, pk):
    def post(self, request, pk):
        form = NewsForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.news = news
            form.save()
            # form.news_id = pk
        return redirect('/')


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


def allnews(request):
    form = NewsForm()
    return render(request, 'services.html', {'form': form})


def about(request):
    return render(request, 'about.html')
