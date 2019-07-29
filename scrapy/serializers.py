from django.db import transaction
from rest_framework import serializers
from scrapy.models import User, ScrappedData


class UserSerializer(serializers.ModelSerializer):
    """Serializer for """

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        user = User.objects.create_user(**validated_data)
        print(user.password)
        return user


class ScrappedSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScrappedData
        fields = ['id', 'source', 'keyword', 'name', 'actual_price', 'selling_price', 'rating', 'image', 'link_product']