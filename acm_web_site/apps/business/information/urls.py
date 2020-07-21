from django.urls import path
from . import views

handler404 = 'apps.business.information.views.page_not_found'

urlpatterns = [
    path('contactus/', views.send_question_email),
    path('awards/', views.AwardList.as_view()),
    # TODO: Create the url for handle reg activity
]