from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__' 아래꺼 말구 이것도 가능하긴 함.
        fields = ['id', 'title', 'body']
        read_only_fields = ('title',)
        # read_only_fields = ('title',)
        # 윗줄 코드 내용 : title 수정불가능 ,쉼표 꼭 써줘야함