
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import CategorySerializer
from newapp.models import Category


class CategoryListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi category qo'shildi"})
        return Response(serializer.errors)


class CategoryEditView(views.APIView):
    permission_classes = (AllowAny,)

    def patch(self, request, id):
        data = request.data
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class CategoryDeleteView(views.APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return Response()
