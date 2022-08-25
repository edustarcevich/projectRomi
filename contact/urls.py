from django.urls import path

from contact.views import Contact_views, Send_email_ok, Mision_and_Vision, History, Groups

urlpatterns = [
    path ("contact/", Contact_views, name="contact"),
    path ("thank/", Send_email_ok, name="thank"),
    path ("mision_and_vision/", Mision_and_Vision, name="mision_and_vision"),
    path ("history/", History, name="history"),
    path ("groups/", Groups, name="groups"),
    
]
