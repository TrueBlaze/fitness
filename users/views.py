from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    """signup new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()

    else:
        # generate a completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # login the user and redirect them to home
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('feelfitness:index'))

    context = {'form': form}
    return render(request, 'users/signup.html', context)








