from django.http import request
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    # return render("H")
    return HttpResponse("Te amo mi Danny <3")