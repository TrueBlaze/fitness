from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Comment
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'feelfitness/index.html', context)


def sign(request):
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = CommentForm
    else:
        # post data submitted; process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return HttpResponseRedirect(reverse('feelfitness:index'))

    context = {'form': form}
    return render(request, 'feelfitness/sign.html', context)


def about(request):
    context = {'request': request}
    return render(request, 'feelfitness/about.html', context)


def portfolio(request):
    context = {'request': request}
    return render(request, 'feelfitness/portfolio.html', context)


def cancer_awareness(request):
    context = {'request': request}
    return render(request, 'feelfitness/cancer_awareness.html', context)


def product_promotion(request):
    context = {'request': request}
    return render(request, 'feelfitness/product_promotion.html', context)


def u_me(request):
    context = {'request': request}
    return render(request, 'feelfitness/u_me.html', context)
