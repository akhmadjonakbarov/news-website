from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers import AccountSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from accountapp.models import Account
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from knox.settings import knox_settings
from rest_framework.serializers import DateTimeField



# axborot tizimining tushunchasi

class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)



# class RegisterView(generics.GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = AccountSerializer

#     def get_token_ttl(self):
#         return knox_settings.TOKEN_TTL

#     def get_expiry_datetime_format(self):
#         return knox_settings.EXPIRY_DATETIME_FORMAT

#     def format_expiry_datetime(self, expiry):
#         datetime_format = self.get_expiry_datetime_format()
#         return DateTimeField(format=datetime_format).to_representation(expiry)

#     def get_post_response_data(self, request, token, instance):
#         data = {
#             'expiry': self.format_expiry_datetime(instance.expiry),
#             'token': token
#         }
#         return data

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         serializer = AccountSerializer(user, many=False)
#         token_ttl = self.get_token_ttl()
#         instance, token = AuthToken.objects.create(user, token_ttl)
#         token = self.get_post_response_data(request, token, instance)

#         return Response(
#             {
#                 "user": serializer.data,
#                 "token": token
#             }
#         )
