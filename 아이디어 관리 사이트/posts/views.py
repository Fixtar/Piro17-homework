from email.mime import image
import json
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Devtool, Post

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if(request.method == 'POST'):
        req = json.loads(request.body)
        try:
            ineter = req['interest']
            Post.objects.filter(id = req['id']).update(interest = ineter)
        except KeyError:
            pass
        ideastar = Post.objects.get(id = req['star']).ideastar
        Post.objects.filter(id = req['star']).update(ideastar = not ideastar)

            
    query = request.GET.get('query',None)
    if query:
        #제목으로 검색
        posts = Post.objects.order_by(query)
    else:
        posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html',context)

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        content = request.POST['content']
        interest = request.POST['interest']
        devtool = Devtool.objects.get(id = request.POST['devtool'])
        
        Post.objects.create(title = title,image = image, content= content, interest=interest, devtool= devtool)

        return redirect('/detail/'+str(Post.objects.latest('id').id))

    devtools = Devtool.objects.all()

    context = {
        'devtools': devtools
    }
    return render(request, 'posts/create.html',context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)

def update(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.interest = request.POST['interest']
        post.devtool = Devtool.objects.get(id = request.POST['devtool'])
        if request.FILES['image']:
            post.image = request.FILES['image']
        else:
            post.image = post.image

        post.save()
        return redirect('/detail/'+str(post.id))
    post = Post.objects.get(id=id)
    devtools = Devtool.objects.all()
    context = {
        'post': post,
        'devtools': devtools
    }
    return render(request, 'posts/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        Post.objects.filter(id = id).delete()
        return redirect('/')
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/delete.html', context)


def devtool(request):
    query = request.GET.get('query',None)
    if query:
        #제목으로 검색
        devtools = Devtool.objects.order_by(query)
    else:
        devtools = Devtool.objects.all()
    context = {
        'devtools': devtools
    }
    return render(request, 'devtools/home.html',context)

def devtoolcreate(request):
    if request.method == 'POST':
        name = request.POST['name']
        kind = request.POST['kind']
        content = request.POST['content']
        Devtool.objects.create(name = name, kind = kind, content = content)
        return redirect('/devtools/detail/'+str(Devtool.objects.latest('id').id))
    context = {}
    return render(request, 'devtools/create.html',context)

def devtooldetail(request, id):
    devtool = Devtool.objects.get(id=id)
    posts = Post.objects.filter(devtool = devtool)
    context = {
        'devtool': devtool,
        'posts': posts
    }
    return render(request, 'devtools/detail.html', context)

def devtoolupdate(request, id):
    if request.method == 'POST':
        devtool = Devtool.objects.get(id=id)
        devtool.name = request.POST['name']
        devtool.kind = request.POST['kind']
        devtool.content = request.POST['content']
        devtool.save()
        return redirect('/devtools/detail/'+str(devtool.id))
    devtool = Devtool.objects.get(id=id)
    context = {
        'devtool': devtool
    }
    return render(request, 'devtools/update.html', context)

def devtooldelete(request, id):
    if request.method == 'POST':
        Devtool.objects.filter(id = id).delete()
        return redirect('/devtools/')
    devtool = Devtool.objects.get(id=id)
    context = {
        'devtool': devtool
    }
    return render(request, 'devtools/delete.html', context)