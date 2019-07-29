from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioPost

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def detail(request, portfolio_id):
    portfolio_detail = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'detail.html', {'portfolios':portfolio_detail})

def new_photo(request):
    return render(request, 'new_photo.html')

def create_photo(request):
    if request.method =='POST':
        form = PortfolioPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # form에 입력된 데이터를 가져온다
            post.title = request.POST['title']
            post.description = request.POST['description']
            post.save()
            return redirect('home')
    else:
        form = PortfolioPost()
        return render(request,'new_photo.html',{'form': form})