from django.shortcuts import redirect
from base62codec.codec import decode
from django.views import View
from .serializers import LinkSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import Link


# Create your views here.
class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortenerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer


class Redirector(View):
    def get(self, request, short_link, *args, **kwargs):
        short_link = self.kwargs['short_link']
        decoded_link_id = decode(short_link)
        redirect_link = Link.objects.get(id=decoded_link_id).source_link
        return redirect(redirect_link)
