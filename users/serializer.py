from  rest_framework import serializers
from users.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','email','password','date_of_birth']