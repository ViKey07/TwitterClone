from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Twitter
from .forms import TwitterForm

# Create your views here.


def home (request):
    # return HttpResponse('hello')
    tweets = Twitter.objects.all()
    if request.method == 'POST':
        form= TwitterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'posts.html', {'tweets':tweets})


def delete(request, post_id):
    #Find post
    post = Twitter.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
# this is for Edit



def edit(request, post_id):
    post = Twitter.objects.get(id=post_id)
    # Find post
    # if request.method == "GET":
    # post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        # editpost = Post.objects.get(id=post_id)
        form = TwitterForm(request.POST, request.FILES, instance=post)
        form.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
    return render(request, 'edit.html', {'post': post})



def LikeView(request, post_id):
    new_value = Twitter.objects.get(id=post_id)
    new_value.likes += 1
    new_value.save()
    return HttpResponseRedirect('/')