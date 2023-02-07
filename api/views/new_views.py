from rest_framework import views
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from api.serializers import (NewSerializer, CommentSerializer,)
from newapp.models import (NewImages, New, Comment,)


class NewListView(views.APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)


class NewAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Yangi new qo'shildi"})
        return Response(serializer.errors)


class NewDetailView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        post = New.objects.get(id=id)
        if post:
            post.updated_views()
        serializer = NewSerializer(post, many=False)
        return Response(serializer.data)


class NewUpdateView(views.APIView):
    permission_classes = (AllowAny, )

    def patch(self, request, id):
        new = New.objects.get(id=request.data['id'])
        serializer = NewSerializer(new, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class NewDeleteView(views.APIView):
    def delete(self, request, id):
        try:
            new = New.objects.get(id=id)
            new.delete()
            return Response({"detail": "success"})
        except Exception as error:
            return Response({"error": error})


class CommentAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "comment was added"})
        return Response(serializer.errors)
