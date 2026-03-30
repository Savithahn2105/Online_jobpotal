from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/register.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        resume = request.FILES['resume']
        Application.objects.create(user=request.user, job=job, resume=resume)
        return redirect('job_list')
    return render(request, 'jobs/apply_job.html', {'job': job})

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'jobs/my_applications.html', {'applications': applications}) 