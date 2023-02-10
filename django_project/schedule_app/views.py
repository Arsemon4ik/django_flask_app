from django.shortcuts import render, redirect
from .models import Schedule


def schedule(request):
    subjects = Schedule.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('subject')

        subjects.update(is_passed=False)
        for id in id_list:
            Schedule.objects.filter(id=int(id)).update(is_passed=True)
        return redirect('schedule')
    else:
        return render(request=request, template_name='schedule.html', context={'subjects': subjects})
