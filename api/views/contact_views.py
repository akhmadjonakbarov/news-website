from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from api.serializers import (ContactSerializer,)


class ContactView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Sizning habaringiz yuborildi."})
        return Response(serializer.data)
