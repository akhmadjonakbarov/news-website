from rest_framework import views
from rest_framework import generics
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response


class RoutesView(views.APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        isGlobal = False
        domain = ''
        g_domain = 'https://news-website-production.up.railway.app/'
        l_domain = 'http://127.0.0.1:8000/'
        if isGlobal:
            domain = g_domain
        else:
            domain = l_domain

        routes = [
            {'GET': f'{domain}api/'},
            {'GET': f'{domain}api/categories/'},
            {'GET':f'{domain}api/news/'},
            {'POST': f'{domain}api/contact/'}
        ]
        return Response(routes)




