from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from .serializers import (CategorySerializer, SubCategorySerializer, )
from postapp.models import (Category,)


class CategoryView(views.APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
