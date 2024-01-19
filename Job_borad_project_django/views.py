from django.shortcuts import render
from django.views.generic import ListView
from job_app.models import EmployeeModel
from service_app.models import ServiceModel



class JobListView(ListView):
    model = EmployeeModel
    template_name = 'home.html'
    context_object_name = 'jobs'

    def get(self, request, *args, **kwargs):
        brand_slug = kwargs.get('brand_slug')
        self.object_list = self.model.objects.all()

        if brand_slug:
            brand = ServiceModel.objects.get(slug=brand_slug)
            self.object_list = self.object_list.filter(brand=brand)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = ServiceModel.objects.all()
        return context