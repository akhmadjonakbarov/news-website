from rest_framework import views
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from serializers import (ContactSerializer,)


class ContactView(views.APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Sizning habaringiz yuborildi."})
        return Response(serializer.data)
