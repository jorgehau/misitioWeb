from django.shortcuts import render
from django.template import RequestContext

from .models import MisDatos

def home(request):
	miapp = MisDatos.objects.all()
	ctx = {'miapp': miapp}
	print ctx
 	return render(request, 'index.html', ctx, 
 		context_instance=RequestContext(request))
