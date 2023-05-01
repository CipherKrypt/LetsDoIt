from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    description = forms.CharField(label = "Description")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "LetsDoIt/index.html", {
        "tasks": request.session["tasks"]
    })

def addtask(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = data["task"]
            desc = data["description"]
            # tasks = request.session["tasks"]
            # tasks.append((task.capitalize(),desc.capitalize())) 
            task = (task.capitalize(), desc.capitalize())
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("LetsDoIt:index"))
        else:
            return render(request, "LetsDoIt/add.html", {
        "form": form
    })
        
    return render(request, "LetsDoIt/add.html", {
        "form": NewTaskForm()
    })
