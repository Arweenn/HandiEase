from django.urls import path
from .views import main, authentication, readingList


urlpatterns = [
    path('', main.home, name='homepage'),
    path('register/', authentication.register_view, name='register_view'),
    path('login/', authentication.login_view, name='login_view'),
    path('logout/', authentication.logout_view, name='logout_view'),
    path('reading_list/', readingList.reading_list, name="reading_list"),
    path('add_to_reading_list/', readingList.add_to_reading_list, name="add_to_reading_list"),
    path('remove_from_reading_list/', readingList.remove_from_reading_list, name="remove_from_reading_list"),
]
