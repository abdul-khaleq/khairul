from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from job_app.models import EmployeeModel,Job_seeker
from job_app.forms import CarModelForm,CommentForm,jobsekeerFrom
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

# Add Car implementation
class AddCreateView(CreateView):
    model = EmployeeModel
    form_class = CarModelForm
    template_name = 'car_app/add_car.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["type"] = "Add"
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong. your car not added in the list.')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Car added successful')
        return super().form_valid(form)
    
# Car details views
from django.contrib.auth.models import User
class CarDetailsView(DetailView):
    model = EmployeeModel
    template_name = 'car_app/car_details.html'
    
    def post(self,request,*args, **kwargs):
        job = self.get_object()
        if self.request.method == 'POST':
            comment_form = CommentForm(data= self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.job = job
                new_comment.save()
                messages.success(self.request, 'Thanks for your opinion!')
            return self.get(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.object
        comments = job.comments.all()
        comment_form = CommentForm()
        context['user_has_applied'] = Job_seeker.objects.filter(user=self.request.user, employee=job).exists()
        context['service'] = self.get_object()
        context['comments'] = comments
        context['form'] = comment_form

        return context

    
class JobSeekerCreateView(CreateView):
    model = Job_seeker
    form_class = jobsekeerFrom
    template_name = 'car_app/job.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        job_seeker = form.save(commit=False)
        job_seeker.user = self.request.user
        job_seeker.save()
        subject = 'Thanks for applying'
        message = f'Hi {self.request.user.first_name} {self.request.user.last_name}, You have applied successfully'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)