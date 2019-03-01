from django.urls import path
from .views import PasteCreate

urlpatterns = [
	path(r'',PasteCreate.as_view(), name='create'),
	]
