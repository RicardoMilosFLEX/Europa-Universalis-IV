from django.shortcuts import render, redirect
from .models import Notes
from .forms import Notesform, UserForm
def index(request):
    return render(request, 'main/main.html')


def forum(request):
    notes = Notes.objects.order_by("-id")
    return render(request,'main/forum.html',{'title':'Форум','notes':notes})
def registration(request):
    return render(request, 'main/registration.html')
def registration_user(request):
    error = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Некорректные данные'
    form = UserForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/registration.html', context)
def enter(request):
    return render(request, 'main/main.html')
#создание записи на сайт
def createnote(request):
    error = ''
    if request.method == 'POST':
        form = Notesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
        else:
            error = 'Запись была не верно заполена'
    form = Notesform()
    context = {'form':form, 'error': error}
    return render(request, 'main/forumcreate.html', context)
