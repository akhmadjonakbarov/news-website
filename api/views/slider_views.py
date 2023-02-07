
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import SliderSerializer
from sliderapp.models import Slider


class SliderView(generics.GenericAPIView):
    serializer_class = SliderSerializer
    permission_classes = (AllowAny,)


class SliderListView(SliderView):

    def get(self, request):
        sliders = Slider.objects.all()
        serializer = self.get_serializer(sliders, many=True)
        return Response(serializer.data)


class SliderAddView(SliderView):

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Yangi slider qo'shildi"})
        return Response(serializer.errors)


class SliderDetailView(SliderView):
    def get(self, request, id):
        slider = Slider.objects.get(id=id)
        serializer = self.get_serializer(slider, many=True)
        return Response(serializer.data)


class SliderEditView(SliderView):

    def patch(self, request, id):
        data = request.data
        slider = Slider.objects.get(id=id)
        serializer = self.get_serializer(slider, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)


class SliderDeleteView(SliderView):

    def delete(self, request, id):
        slider = Slider.objects.get(id=id)
        slider.delete()
        return Response()
