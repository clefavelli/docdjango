#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Board
from django.template import loader

def index(request):
	distributor_list = Board.objects.all()
	template = loader.get_template('djangomen/index.html')
	context = {'distributor_list': distributor_list,}
	return HttpResponse(template.render(context, request))
	#output = ', '.join([d.name for d in distributor_list])
	#return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")

def distributor(request, board_id):
    return HttpResponse("You're looking at distributor %s." % board_id)