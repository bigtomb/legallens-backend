from xml.dom.minidom import Document
from rest_framework import serializers

from api.models import Analyses
from authentication.serializers import UserSerializer


class DocumentSerializer(serializers.Serializer):
    document = serializers.FileField()

class AnalysisSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Analyses
        fields = '__all__'