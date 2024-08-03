from rest_framework import serializers
from .models import Client, SignatureList, Signature

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ['id', 'imagem_base64', 'created_at']

class SignatureListSerializer(serializers.ModelSerializer):
    signatures = SignatureSerializer(many=True, read_only=True)

    class Meta:
        model = SignatureList
        fields = ['id', 'name', 'owner', 'signatures', 'created_at']

class ClientSerializer(serializers.ModelSerializer):
    signature_lists = SignatureListSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'user', 'is_owner', 'signature_lists']