from django.shortcuts import render, redirect


def dashboard(request):
    if request.user_is_authenticated:
        return redirect('user_home')
    else:
        return render(request, 'dashboard/welcome.html')