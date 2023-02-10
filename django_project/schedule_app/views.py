from django.shortcuts import render, redirect
from .models import Schedule


def schedule(request):
    """ Schedule function for take request and send response back via html template
    Args:
        request: [The request parameter is a HttpRequest object]
    Returns:
        render: [Rendered HTML template],
        redirect: [Redirected to the same page to reload]
    """

    subjects = Schedule.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('subject')

        subjects.update(is_passed=False)
        for id in id_list:
            Schedule.objects.filter(id=int(id)).update(is_passed=True)
        return redirect('schedule')
    else:
        return render(request=request, template_name='schedule.html', context={'subjects': subjects})
