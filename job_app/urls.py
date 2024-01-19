from django.urls import path
from job_app.views import AddCreateView,CarDetailsView,JobSeekerCreateView

urlpatterns = [
    path('add_car/', AddCreateView.as_view(), name='add_car' ),
    path('car_details/<int:pk>/', CarDetailsView.as_view(), name='car_details' ),
    path('job/', JobSeekerCreateView.as_view(), name='job_seeker' )
]
