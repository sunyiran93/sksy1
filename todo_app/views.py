from turtle import title
from django.shortcuts import render, redirect
from .models import Task, Imprint
from django.shortcuts import render, get_object_or_404
from .forms import ImprintForm
# Create your views here.


# This is a overview page where you can see all the task, can see update and delete button.
def overview(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }
    return render(request, 'overview.html', context)



# This is a imprint page where you can see all authors.
def imprint(request):
    imprints = Imprint.objects.get()

    context = {
        'imprints': imprints,
    }
    return render(request, 'imprint.html', context)



# This is a function view to update your imprint.
def updateImprint(request, pk):
    imprints = Imprint.objects.get(id=pk)
    form = ImprintForm(instance=imprints)

    if request.method == 'POST':
        form = ImprintForm(request.POST, instance=imprints)
        if form.is_valid():
            form.save()
            return redirect('imprint')

    context = {
        'form': form
    }
    return render(request, 'imprint_form.html', context)



# This is a function view for create/add task.
def createTask(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        progress = request.POST['progress']
        b = Task.objects.create(
                title=title,
                date=date,
                progress=progress)
        b.save()
        return redirect('overview')
    return render(request, 'task_form.html')


# This is a function view to update an individual task.
def updateTask(request, id):
    task_obj= get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('date') and request.POST.get('progress'):
            Task.objects.filter(id = id).update(title= request.POST.get('title'), date= request.POST.get('date'), progress=request.POST.get('progress'))
            # context={'task_obj': task_obj}
            # return render(request, 'task_edit_form.html')  
            return redirect('overview')

    else:
        context={
            'task_obj': task_obj,
        }
        return render(request,'task_edit_form.html', context)

    # else:
    #     context={'task_obj': task_obj,
    #     'error': 'The post was not successfully updated. The title and content must be filled out.'}
    #     return render(request,'task_edit_form.html', context)


# This is for delete an individual task.
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('overview')
    context = {
        'object': task
    }
    return render(request, 'delete_template.html', context)
