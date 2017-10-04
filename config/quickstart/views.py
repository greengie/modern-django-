from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from config.quickstart.serializers import UserSerializer, GroupSerializer, TestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import json
import math
from django.http import HttpResponse, HttpResponseRedirect
import os
from config.quickstart.utils import makeprediction

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TestPrediction(APIView):

    def get(self, request, *args, **kw):
        print("calling get method")
        response = Response('GET', status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        # print(type(request.body.decode("utf-8")))
        # print(request.data)
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        # msg_body = json.loads(request.body.decode("utf-8"))
        # print("msg_body: {}".format(msg_body))
        # print(type(msg_body))
        # ip_id = msg_body['id']
        # prediction_class = makeprediction.get_feature(ip_id)
        # print ("Class is : " + str(prediction_class['value']))
        response = Response("POST", status=status.HTTP_200_OK)
        return response
