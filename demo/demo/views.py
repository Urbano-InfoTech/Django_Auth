from dj_rest_auth.registration.views import RegisterView
from .serializers import ExtendSerializer


class ExtendView(RegisterView):
    serializer_class = ExtendSerializer
    def create(self, request, *args, **kwargs):
        print('hello')
        return super().create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     super.create(self, request, *args, **kwargs)
    #     print('hello')
    
