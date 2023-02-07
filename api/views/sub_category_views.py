
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import SubCategorySerializer
from newapp.models import SubCategory


class SubCategoryView(generics.GenericAPIView):
    serializer_class = SubCategorySerializer
    permission_classes = (AllowAny,)


class SubCategoryListView(SubCategoryView):

    def get(self, request):
        sub_categories = SubCategory.objects.all()
        serializer = self.get_serializer(sub_categories, many=True)
        return Response(serializer.data)


class SubCategoryAddView(SubCategoryView):
    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi SubCategory qo'shildi"})
        return Response(serializer.errors)


class SubCategoryEditView(SubCategoryView):

    def patch(self, request, id):
        data = request.data
        sub_category = SubCategory.objects.get(id=id)
        serializer = self.get_serializer(
            sub_category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SubCategoryDeleteView(SubCategoryView):

    def delete(self, request, id):
        id = self.request.query_params.get("id")
        sub_category = SubCategory.objects.get(id=id)
        sub_category.delete()
        return Response({"message": "success"})
