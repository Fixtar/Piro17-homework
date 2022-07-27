import json
from django.shortcuts import render,redirect
from .models import comment
from .forms import CommentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
    else:
        comments = comment.objects.all()
        context = {
            'comments': comments
        }
        return render(request, 'home.html', context)

    comments = comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'home.html',context)
    
@csrf_exempt
def like(request):
    req = json.loads(request.body)
    comment_id = req['commentId']
    comment1 = comment.objects.get(id=comment_id)
    comment1.like = not comment1.like
    comment1.save()
    return JsonResponse({ 'commentId': comment_id})

@csrf_exempt
def delete(request):
    req = json.loads(request.body)
    comment_id = req['commentId']
    comment.objects.filter(id=comment_id).delete()
    return JsonResponse({ 'commentId': comment_id })