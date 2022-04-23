from rest_framework.serializers import ModelSerializer
from .models import Users


# class AuthorsModelSerializers(HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'


class AuthorsModelSerializers(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'birthday_year', 'email', 'position')
        # exclude = ('uid',)


class AuthorsModelSerializersMore(ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'birthday_year', 'email', 'position', 'is_staff', 'is_superuser')
        # exclude = ('uid',)
