
from rest_framework import generics
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from api.serializers import (NewSerializer, CommentSerializer, NewSerializerMobile)
from newapp.models import (NewImages, New, Comment,)


class NewView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = NewSerializer


class NewListView(NewView):

    def get(self, request):
        news = New.objects.all()
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)


class NewAddView(NewView):

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Yangi new qo'shildi"})
        return Response(serializer.errors)


class NewDetailView(NewView):
    def get(self, request, id):
        post = New.objects.get(id=id)
        if post:
            post.updated_views()
        serializer = self.get_serializer(post, many=False)
        return Response(serializer.data)


class NewUpdateView(NewView):

    def patch(self, request, id):
        new = New.objects.get(id=request.data['id'])
        serializer = self.get_serializer(new, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class NewDeleteView(NewView):
    def delete(self, request, id):
        try:
            new = New.objects.get(id=id)
            new.delete()
            return Response({"detail": "success"})
        except Exception as error:
            return Response({"error": error})


class CommentAddView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "comment was added"})
        return Response(serializer.errors)


class NewMobileListView(generics.GenericAPIView):
    serializer_class = NewSerializerMobile
    permission_classes = (AllowAny,)

    def get(self, request):
        news = New.objects.all()
        serializer = self.get_serializer(news, many=True)
        return Response(serializer.data)