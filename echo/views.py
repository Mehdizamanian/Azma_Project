from django.shortcuts import render , HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OsCommand , MathCommand
from .serializers import *


def index(request):
  return render(request,'echo/index.html')


@api_view(["GET"])
def api(request):
  queries=MathCommand.objects.all()
  queries_serializer=MathCommandSerializer(queries,many=True)
  return Response (queries_serializer.data)

# Create your views here.
