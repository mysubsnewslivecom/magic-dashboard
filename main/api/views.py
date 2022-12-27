from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests

class ISSLocation(ViewSet):
    def list(self, request, *args, **kwargs):

        resp = requests.request(method="GET", url="http://api.open-notify.org/iss-now.json")
        print(resp)
        return Response(resp.json())


