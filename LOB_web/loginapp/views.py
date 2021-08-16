from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm
from django.contrib import messages


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/appcenter")
    else:
        # Puxando form.
        form = LoginForm(request.POST or None)
        context = {"form": form}

        #print("User logged in")
        #print(request.user.is_authenticated)

        # Veficando se os dados são válidos, primeiro authenticate e depois login.
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            # print(user)
            # print(request.user.is_authenticated)

            if user is not None:
                login(request, user)
                print(request.user.is_authenticated)
                print("Valid login")
                # Redireciona para uma página de sucesso.
                return redirect("/appcenter")
            else:
                # Retorna uma mensagem de erro de 'invalid login'.
                print("Invalid login")
                messages.error(request,'Incorrect username or password.')
                return redirect("/login")

        return render(request, "login_app/login.html", context)

def logout_page(request):
    # if request.method == "POST":
    messages.error(request, 'Disconnected user.')
    logout(request)
    return redirect("/login")
    # return render(request, "login_app/logout.html")

# O get_user_model serve para retornar o model de user ativo no momento.
User = get_user_model()


