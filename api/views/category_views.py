
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from serializers import CategorySerializer
from postapp.models import Category


class CategoryListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        pass


class CategoryEditView(views.APIView):
    permission_classes = (AllowAny,)

    def patch(self, request):
        pass


class CategoryDeleteView(views.APIView):
    permission_classes = (AllowAny,)

    def delete(self, request):
        pass
