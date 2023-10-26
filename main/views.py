from django.shortcuts import render, redirect
from .models import Notes
from .forms import Notesform
def index(request):
    return render(request, 'main/main.html')


def forum(request):
    notes = Notes.objects.order_by("-id")
    return render(request,'main/forum.html',{'title':'Форум','notes':notes})


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