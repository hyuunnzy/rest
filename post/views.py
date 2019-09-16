from rest_framework import viewsets

from .models import Post
from .serializer import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # POST에서 다 가져오겠다.
    serializer_class = PostSerializer


# Create your views here.
