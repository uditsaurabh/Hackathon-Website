from Register_App.models import Team
from rest_framework import serializers

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields = '__all__'
