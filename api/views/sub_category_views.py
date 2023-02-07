
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import SubCategorySerializer
from newapp.models import SubCategory


class SubCategoryListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        sub_categories = SubCategory.objects.all()
        serializer = SubCategorySerializer(sub_categories, many=True)
        return Response(serializer.data)


class SubCategoryAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = SubCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi SubCategory qo'shildi"})
        return Response(serializer.errors)


class SubCategoryEditView(views.APIView):
    permission_classes = (AllowAny,)

    def patch(self, request, id):
        data = request.data
        sub_category = SubCategory.objects.get(id=id)
        serializer = SubCategorySerializer(sub_category, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SubCategoryDeleteView(views.APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, id):
        id =self.request.query_params.get("id")
        sub_category = SubCategory.objects.get(id=id)
        sub_category.delete()
        return Response({"message":"success"})
