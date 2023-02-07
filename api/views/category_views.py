
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import CategorySerializer
from newapp.models import Category


class CategoryView(generics.GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class CategoryListView(CategoryView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()

    def get(self, request):
        categories = Category.objects.all()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class CategoryAddView(CategoryView):
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi category qo'shildi"})
        return Response(serializer.errors)


class CategoryEditView(CategoryView):

    def patch(self, request, id):
        data = request.data
        category = Category.objects.get(id=id)
        serializer = self.get_serializer(category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class CategoryDeleteView(CategoryView):

    def delete(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return Response()
