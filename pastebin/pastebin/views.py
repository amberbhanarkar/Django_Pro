from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
class PasteCreate(CreateView):
	model = Paste		
	fields = ['text', 'name']
