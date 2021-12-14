from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Home(APIView):
    """
    Landing endpoint if no path is specified.
    """
    def get(self, request):
        return Response({"message": "Hey! Checkout the documentation here URL"}, status=status.HTTP_200_OK)