from rest_framework import serializers
from User.models import User, Address, Interests, Schools, Colleges, Courses
from django.contrib.auth import update_session_auth_hash


class AddressSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Address
        fields = ('id', 'addressLine1', 'addressLine2', 'city', 'state_province', 'modified_at')

        read_only_fields = ('id', 'modified_at')

        def create(self, validated_data):
            return Address.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.addressLine1 = validated_data.get('addressLine1', instance.addressLine1)
            instance.addressLine2 = validated_data.get('addressLine2', instance.addressLine2)
            instance.city = validated_data.get('city', instance.city)
            instance.state_province = validated_data.get('state_province', instance.state_province)

            instance.save()
            return instance

    def get_validation_exclusion(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    address = AddressSerializer(required=False)
    education_level = serializers.CharField(required=False)
    
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'joined_at', 'modified_at',
                  'first_name', 'last_name', 'description', 'password',
                  'confirm_password', 'birthdate', 'is_tutor', 'education_level',
                  'address')

        read_only_fields = ('joined_at', 'modified_at')

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.email = validated_data.get('email', instance.username)
            instance.description = validated_data.get('description', instance.description)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.description = validated_data.get('description', instance.description)
            instance.birthdate = validated_data.get('birthdate', instance.birthdate)
            instance.is_tutor = validated_data.get('is_tutor', instance.is_tutor)
            instance.education_level = validated_data.get('education_level', instance.education_level)
            instance.address = validated_data.get('address', instance.address)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            upadate_session_auth_hash(self.context.get('request'), instance)

            return instance


            
class InterestsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    
    class Meta:
        model = Interests
        fields = ('id', 'interest')

        def create(self, validated_data):
            return Interests.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.interest = validated_data.get('interest', instance.interest)
            instance.save()
            return instance


class SchoolsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    
    class Meta:
        model = Schools
        fields = ('id', 'name', 'highest_grade')

        def create(self, validated_data):
            return Schools.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.highest_grade = validated_data.get('highest_grade', instance.highest_grade)
            instance.save()
            return instance

class CollegesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Schools
        fields = ('id', 'name', 'highest_degreee')

        def create(self, validated_data):
            return Colleges.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.highest_grade = validated_data.get('highest_grade', instance.highest_grade)
            instance.save()
            return instance


class CoursesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model=Courses
        fields = ('id', 'course', 'offered')

        def create(self, validated_data):
            return Courses.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.course = validated_data.get('course', instance.name)
            instance.highest_grade = validated_data.get('offered', instance.highest_grade)
            instance.save()
            return instance
                
