from django.urls import path
from job_app.views import AddJobCreateView,JobDetailsView,JobSeekerCreateView

urlpatterns = [
    path('add_job/', AddJobCreateView.as_view(), name='add_job' ),
    path('job_details/<int:pk>/', JobDetailsView.as_view(), name='job_details' ),
    path('job/', JobSeekerCreateView.as_view(), name='job_seeker' )
]
