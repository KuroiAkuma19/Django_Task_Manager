from rest_framework import serializers 
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = ('id','title','description','completed')


from rest_framework import serializers
from .models import Todo  # Ensure you import the correct model

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'  # <-- Add this line
