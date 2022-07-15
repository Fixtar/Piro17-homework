from multiprocessing import context
from turtle import title
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def home(request):
    query = request.GET.get('query',None)
    if query:
        #제목으로 검색
        reviews = Review.objects.order_by(query)
    else:
        reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/home.html',context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        openyear = request.POST.get('openyear')
        genre = request.POST.get('genre')
        starpoint = request.POST.get('starpoint')
        director = request.POST.get('director')
        actor = request.POST.get('actor')
        runningtime = request.POST.get('runningtime')
        review = request.POST.get('review')
        Review.objects.create(title=title, openyear=openyear, genre=genre, starpoint=starpoint, director=director, actor=actor, runningtime=runningtime, review=review)

        return redirect('/')

    context = {
        'category': Review.genrecategory
    }
    return render(request, 'reviews/create.html',context)


def detail(request, id):
    #Post라는 class의 객체들 중에 id를 가진 객체를 찾아옴
    review = Review.objects.get(id=id)
    context = {
        'review': review
    }
    return render(request, template_name='reviews/detail.html', context = context)


def update(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        openyear = request.POST['openyear']
        genre = request.POST['genre']
        starpoint = request.POST['starpoint']
        director = request.POST['director']
        actor = request.POST['actor']
        runningtime = request.POST['runningtime']
        review = request.POST['review']


        Review.objects.filter(id = id).update(title=title, openyear=openyear, genre=genre, starpoint=starpoint, director=director, actor=actor, runningtime=runningtime, review=review)
        return redirect('/detail/'+str(id))

    review = Review.objects.get(id=id)
    context = {
        'review': review
    }
    return render(request, template_name='reviews/update.html', context = context)

def delete(request, id):
    if request.method == 'POST':
        Review.objects.filter(id = id).delete()
        return redirect('/')