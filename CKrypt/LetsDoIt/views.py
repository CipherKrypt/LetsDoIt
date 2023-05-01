from django.shortcuts import render

tasks = ["task1", "task2", "task3"]
def index(request):
    return render(request, "LetsDoIt/index.html", {
        "tasks": tasks
    })
