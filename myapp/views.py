from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from myapp.models import Restorent
from myapp.serializers import RestorentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

def index(request):
	return render(request, "index.html")

class RestorentList(ListCreateAPIView):
	queryset = Restorent.objects.all()
	serializer_class = RestorentSerializer

class RUDRestorentList(RetrieveUpdateDestroyAPIView):
	queryset = Restorent.objects.all()
	serializer_class = RestorentSerializer






