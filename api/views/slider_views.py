
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import SliderSerializer
from sliderapp.models import Slider


class SliderListView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)


class SliderAddView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = SliderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi slider qo'shildi"})
        return Response(serializer.errors)


class SliderDetailView(views.APIView):
    def get(self, request, id):
        slider= Slider.objects.get(id=id)
        serializer = SliderSerializer(slider, many=True)
        return Response(serializer.data)

class SliderEditView(views.APIView):
    permission_classes = (AllowAny,)

    def patch(self, request, id):
        data = request.data
        slider = Slider.objects.get(id=id)
        serializer = SliderSerializer(slider, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class SliderDeleteView(views.APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, id):
        slider = Slider.objects.get(id=id)
        slider.delete()
        return Response()
