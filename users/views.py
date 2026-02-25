from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('item_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('item_list')